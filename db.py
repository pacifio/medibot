import asyncio
import time
from typing import List, Dict, Any
import numpy as np
from doctors import DOCTORS, Doctor
from fastembed import TextEmbedding
import antarys


class DoctorVectorizer:
    def __init__(self, host: str = "http://localhost:8080"):
        self.host = host
        self.client = None
        self.embedding_model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5")
        self.collection_name = "doctors"

    async def initialize_client(self):
        self.client = await antarys.create_client(
            host=self.host,
            timeout=120,
            debug=True,
            use_http2=True,
            cache_size=1000,
            connection_pool_size=50,
            thread_pool_size=8
        )
        print(f"Connected to Antarys at {self.host}")

    def create_doctor_text(self, doctor: Doctor) -> str:
        degrees_str = ", ".join(doctor.degrees)

        doctor_text = f"""
        Dr. {doctor.name} is a {doctor.specialisation} specialist.
        Specialization: {doctor.specialisation}
        Medical Degrees: {degrees_str}
        Hospital: {doctor.hospital}
        Gender: {doctor.sex}
        Age: {doctor.age} years old
        Contact: {doctor.phone}
        Email: {doctor.email}
        Booking: {doctor.booking_url}
        
        Medical expertise includes treatment of conditions related to {doctor.specialisation.lower()}.
        Available for consultation and treatment in {doctor.hospital}.
        """.strip()

        return doctor_text

    def vectorize_doctors(self, doctors: List[Doctor]) -> List[Dict[str, Any]]:
        print("Creating text representations...")
        doctor_texts = [self.create_doctor_text(doctor) for doctor in doctors]

        print("Generating embeddings...")
        embeddings = list(self.embedding_model.embed(doctor_texts))

        vector_records = []
        for i, (doctor, embedding) in enumerate(zip(doctors, embeddings)):
            vector_values = embedding.tolist() if hasattr(
                embedding, 'tolist') else list(embedding)

            record = {
                "id": f"doctor_{i}",
                "vector": vector_values,
                "metadata": {
                    "name": doctor.name,
                    "specialisation": doctor.specialisation,
                    "degrees": doctor.degrees,
                    "hospital": doctor.hospital,
                    "age": doctor.age,
                    "sex": doctor.sex,
                    "phone": doctor.phone,
                    "email": doctor.email,
                    "booking_url": doctor.booking_url,
                    "searchable_text": self.create_doctor_text(doctor)
                }
            }
            vector_records.append(record)

        print(f"Generated {len(vector_records)} doctor vectors")
        return vector_records

    async def create_collection(self):
        try:
            sample_embedding = list(
                self.embedding_model.embed(["sample text"]))[0]
            dimensions = len(sample_embedding.tolist() if hasattr(
                sample_embedding, 'tolist') else list(sample_embedding))

            print(
                f"Creating collection '{self.collection_name}' with {dimensions} dimensions...")

            result = await self.client.create_collection(
                name=self.collection_name,
                dimensions=dimensions,
                enable_hnsw=True,
                shards=16,
                m=16,
                ef_construction=200
            )

            if result.get("success"):
                print(
                    f"Collection '{self.collection_name}' created successfully")
            else:
                print(f"Collection creation result: {result}")

        except Exception as e:
            if "already exists" in str(e).lower():
                print(f"Collection '{self.collection_name}' already exists")
            else:
                print(f"Error creating collection: {e}")
                raise

    async def upload_doctors(self, vector_records: List[Dict[str, Any]]):
        try:
            print(f"🔄 Uploading {len(vector_records)} doctor records...")

            vectors = self.client.vector_operations(self.collection_name)

            result = await vectors.upsert(
                vectors=vector_records,
                batch_size=100,
                show_progress=True,
                parallel_workers=4,
                validate_dimensions=True
            )

            print(
                f"Successfully uploaded {result.get('upserted_count', 0)} doctor records")

        except Exception as e:
            print(f"Error uploading doctors: {e}")
            raise

    async def setup_database(self):
        print("Starting doctor database setup...")

        try:
            await self.initialize_client()
            await self.create_collection()

            vector_records = self.vectorize_doctors(DOCTORS)
            await self.upload_doctors(vector_records)

            print("Database setup completed successfully!")

        except Exception as e:
            print(f"Database setup failed: {e}")
            raise
        finally:
            if self.client:
                await self.client.close()


async def main():
    vectorizer = DoctorVectorizer()
    await vectorizer.setup_database()


if __name__ == "__main__":
    asyncio.run(main())

import streamlit as st
from streamlit_chat import message
import asyncio
import time
import re
from typing import List, Dict, Any, Optional
import openai
from fastembed import TextEmbedding
import antarys
from dataclasses import dataclass


@dataclass
class DiseaseAssessment:
    disease: str
    probability: float
    description: str


@dataclass
class DoctorRecommendation:
    name: str
    specialisation: str
    hospital: str
    phone: str
    email: str
    booking_url: str
    relevance_score: float
    degrees: List[str]


class MedicalChatbot:
    def __init__(self, antarys_host: str = "http://localhost:8080"):
        self.openai_client = openai.OpenAI()
        self.antarys_host = antarys_host
        self.antarys_client = None
        self.embedding_model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5")
        self.collection_name = "doctors"

        self.medical_keywords = {
            'symptoms': ['pain', 'ache', 'fever', 'headache', 'nausea', 'vomiting', 'diarrhea',
                         'constipation', 'cough', 'cold', 'flu', 'sore throat', 'chest pain',
                         'stomach pain', 'back pain', 'joint pain', 'muscle pain', 'fatigue',
                         'dizziness', 'shortness of breath', 'palpitations', 'rash', 'itching',
                         'swelling', 'bleeding', 'bruising', 'numbness', 'tingling', 'weakness'],
            'body_parts': ['head', 'brain', 'eye', 'ear', 'nose', 'throat', 'neck', 'chest',
                           'heart', 'lung', 'stomach', 'abdomen', 'liver', 'kidney', 'back',
                           'spine', 'arm', 'leg', 'hand', 'foot', 'skin', 'bone', 'joint',
                           'muscle', 'blood', 'nerve'],
            'conditions': ['diabetes', 'hypertension', 'cancer', 'infection', 'allergy',
                           'asthma', 'arthritis', 'depression', 'anxiety', 'migraine',
                           'epilepsy', 'stroke', 'heart attack', 'pneumonia', 'bronchitis']
        }

    async def initialize(self):
        try:
            self.antarys_client = await antarys.create_client(
                host=self.antarys_host,
                timeout=60,
                debug=False,
                cache_size=500
            )
            return True
        except Exception as e:
            st.error(f"Failed to connect to Antarys: {e}")
            return False

    async def is_medical_query(self, query: str, chat_history: List[Dict] = None) -> bool:
        chat_history = chat_history or []

        context = ""
        if chat_history:
            recent_context = chat_history[-3:]  # Last 3 exchanges for context
            context = "\n".join(
                [f"User: {chat['user']}\nBot: {chat['bot'][:200]}..." for chat in recent_context])

        classification_prompt = f"""
        Analyze the following user message and determine if it's a medical query that requires symptom assessment and doctor recommendations.
        
        Chat context (recent conversation):
        {context}
        
        Current user message: "{query}"
        
        A medical query is one where the user is:
        - Describing physical symptoms or health problems
        - Asking for medical advice about symptoms
        - Seeking help for a health condition
        - Requesting doctor recommendations for a specific medical issue
        - Following up on previous medical discussions with related questions
        
        NOT medical queries:
        - General conversations about health (like "is exercise good?")
        - Thanking or casual responses
        - General questions not about specific symptoms
        - Philosophical or general health discussions
        
        Consider the conversation context - if the user previously discussed medical symptoms and is now asking follow-up questions about doctors or treatment, this should be considered medical.
        
        Respond with only "YES" if this requires medical assessment and doctor recommendations, or "NO" if it's a general conversation.
        """

        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a medical query classifier. Consider conversation context. Respond only with YES or NO."},
                    {"role": "user", "content": classification_prompt}
                ],
                max_tokens=10,
                temperature=0.1
            )

            result = response.choices[0].message.content.strip().upper()
            return result == "YES"

        except Exception as e:
            return False

    async def assess_symptoms(self, query: str, chat_history: List[Dict] = None) -> List[DiseaseAssessment]:
        chat_history = chat_history or []

        context = ""
        if chat_history:
            recent_medical = [chat for chat in chat_history[-5:]
                              if "Medical Assessment" in chat.get('bot', '')]
            if recent_medical:
                context = f"Previous medical context: {recent_medical[-1]['user']} - {recent_medical[-1]['bot'][:300]}..."

        assessment_prompt = f"""
        You are a medical AI assistant. Based on the following patient query and conversation context, provide a preliminary assessment of possible conditions.
        
        {context}
        
        Current Patient Query: "{query}"
        
        Please provide up to 5 possible conditions with probability percentages. Format your response as:
        
        Disease: [Disease Name] | Probability: [X%] | Description: [Brief description]
        
        Important: This is for preliminary assessment only and should not replace professional medical diagnosis.
        Be conservative with probabilities and always recommend consulting a healthcare professional.
        
        If this is a follow-up question about a previous medical discussion, focus on the original symptoms and condition.
        
        Example format:
        Disease: Viral Fever | Probability: 65% | Description: Common viral infection with fever and body aches
        Disease: Bacterial Infection | Probability: 25% | Description: Possible bacterial infection requiring antibiotic treatment
        """

        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful medical AI assistant providing preliminary symptom assessment with conversation context."},
                    {"role": "user", "content": assessment_prompt}
                ],
                max_tokens=500,
                temperature=0.3
            )

            assessment_text = response.choices[0].message.content
            return self._parse_assessment(assessment_text)

        except Exception as e:
            st.error(f"Error in symptom assessment: {e}")
            return [DiseaseAssessment("General Health Concern", 50.0, "Unable to assess symptoms. Please consult a healthcare professional.")]

    def _parse_assessment(self, assessment_text: str) -> List[DiseaseAssessment]:
        assessments = []
        pattern = r"Disease:\s*([^|]+)\s*\|\s*Probability:\s*(\d+)%\s*\|\s*Description:\s*([^|\n]+)"
        matches = re.findall(pattern, assessment_text, re.IGNORECASE)

        for match in matches:
            disease = match[0].strip()
            probability = float(match[1])
            description = match[2].strip()
            assessments.append(DiseaseAssessment(
                disease, probability, description))

        if not assessments:
            assessments.append(
                DiseaseAssessment("General Health Concern", 50.0,
                                  "Please consult a healthcare professional for proper diagnosis.")
            )

        return assessments

    async def find_relevant_doctors(self, query: str, chat_history: List[Dict] = None, top_k: int = 5) -> tuple[List[DoctorRecommendation], float]:
        try:
            start_time = time.time()

            # Build enhanced query with context
            search_query = query
            if chat_history:
                recent_medical = [chat for chat in chat_history[-3:]
                                  if "Medical Assessment" in chat.get('bot', '')]
                if recent_medical:
                    original_symptoms = recent_medical[-1]['user']
                    search_query = f"{original_symptoms} {query}"

            query_embedding = list(
                self.embedding_model.embed([search_query]))[0]
            query_vector = query_embedding.tolist() if hasattr(
                query_embedding, 'tolist') else list(query_embedding)

            vectors = self.antarys_client.vector_operations(
                self.collection_name)

            results = await vectors.query(
                vector=query_vector,
                top_k=top_k,
                include_metadata=True,
                use_ann=True,
                threshold=0.0
            )

            search_time = time.time() - start_time

            recommendations = []
            for match in results.get('matches', []):
                metadata = match.get('metadata', {})
                score = match.get('score', 0.0)

                recommendation = DoctorRecommendation(
                    name=metadata.get('name', 'Unknown'),
                    specialisation=metadata.get('specialisation', 'General'),
                    hospital=metadata.get('hospital', 'Unknown Hospital'),
                    phone=metadata.get('phone', 'N/A'),
                    email=metadata.get('email', 'N/A'),
                    booking_url=metadata.get('booking_url', 'N/A'),
                    relevance_score=score,
                    degrees=metadata.get('degrees', [])
                )

                recommendations.append(recommendation)

            return recommendations, search_time

        except Exception as e:
            st.error(f"Error finding doctors: {e}")
            return [], 0.0

    async def general_chat(self, user_query: str, chat_history: List[Dict]) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant. You can discuss any topic and provide general assistance. If users ask about medical symptoms or health concerns, you can also help assess symptoms and recommend verified doctors from your platform."}
        ]

        for chat in chat_history:
            messages.append({"role": "user", "content": chat["user"]})
            messages.append({"role": "assistant", "content": chat["bot"]})

        messages.append({"role": "user", "content": user_query})

        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in chat: {e}"

    async def process_query(self, user_query: str, chat_history: List[Dict] = None) -> tuple:
        chat_history = chat_history or []

        is_medical = await self.is_medical_query(user_query, chat_history)

        if is_medical:
            try:
                assessments = await self.assess_symptoms(user_query, chat_history)
                doctors, search_time = await self.find_relevant_doctors(user_query, chat_history)
                return assessments, doctors, search_time, None, True
            except Exception as e:
                error_msg = f"Error processing medical query: {e}"
                return None, None, 0.0, error_msg, True
        else:
            try:
                general_response = await self.general_chat(user_query, chat_history)
                return None, None, 0.0, general_response, False
            except Exception as e:
                error_msg = f"Error in general chat: {e}"
                return None, None, 0.0, error_msg, False

    async def close(self):
        if self.antarys_client:
            await self.antarys_client.close()


def format_response(assessments, doctors, search_time, general_response, is_medical):
    if not is_medical:
        return general_response

    response = ""

    if assessments:
        response += "**Medical Assessment:**\n\n"
        for assessment in assessments:
            response += f"• **{assessment.disease}** - {assessment.probability:.0f}% likely\n"
            response += f"  {assessment.description}\n\n"

    if doctors:
        response += "**Verified Doctors on Our Platform:**\n\n"
        for i, doctor in enumerate(doctors, 1):
            relevance_percent = doctor.relevance_score * 100
            degrees_str = ", ".join(doctor.degrees)

            response += f"**{i}. {doctor.name}** - {doctor.specialisation}\n"
            response += f"Relevance: {relevance_percent:.1f}% | {doctor.hospital}\n"
            response += f"Degrees: {degrees_str}\n"
            response += f"Phone: {doctor.phone} | Email: {doctor.email}\n"
            response += f"[Book Appointment]({doctor.booking_url})\n\n"

    if search_time > 0:
        response += f"*Doctor search completed in {search_time:.3f} seconds*"

    return response


def on_input_change():
    user_input = st.session_state.user_input
    if user_input.strip():
        st.session_state.past.append(user_input)

        chat_history = []
        for i in range(len(st.session_state.past) - 1):
            chat_history.append({
                "user": st.session_state.past[i],
                "bot": st.session_state.generated[i] if i < len(st.session_state.generated) else ""
            })

        with st.spinner("Processing..."):
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                assessments, doctors, search_time, general_response, is_medical = loop.run_until_complete(
                    st.session_state.chatbot.process_query(
                        user_input, chat_history)
                )

                response = format_response(
                    assessments, doctors, search_time, general_response, is_medical)
                st.session_state.generated.append(response)

            except Exception as e:
                st.session_state.generated.append(f"Error: {e}")

        st.session_state.user_input = ""


def on_clear_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


async def initialize_chatbot():
    if 'chatbot' not in st.session_state or not st.session_state.get('initialized', False):
        chatbot = MedicalChatbot()
        success = await chatbot.initialize()
        if success:
            st.session_state.chatbot = chatbot
            st.session_state.initialized = True
            return True
        return False
    return True


st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🏥"
)

st.title("Medical Chatbot")

if 'past' not in st.session_state:
    st.session_state.past = []

if 'generated' not in st.session_state:
    st.session_state.generated = []

if not st.session_state.get('initialized', False):
    with st.spinner("Initializing chatbot..."):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            success = loop.run_until_complete(initialize_chatbot())
            if success:
                st.success("Chatbot ready!")
            else:
                st.error("Failed to initialize chatbot.")
                st.stop()
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

st.warning("AI Assistant with verified doctor recommendations for health concerns.")

chat_placeholder = st.empty()

with chat_placeholder.container():
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
            message(st.session_state['generated'][i], key=f"{i}")

with st.container():
    st.text_input("Enter your symptoms:", on_change=on_input_change,
                  key="user_input", placeholder="Describe your symptoms or health concerns...")
    st.button("Clear Chat", on_click=on_clear_click)

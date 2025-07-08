## Medibot

Simple medical bot for getting doctor recommendations and early diagnosis based on symptoms

you will need OPENAI API key for this.

### How to use this

1. git clone the repo
2. cd medibot
3. donwload the binary from [Antarys](http://antarys.ai/)
4. run the following

```commandline
./antarys \
  --port=8080 \
  --data-dir=./data \
  --enable-gpu=false \
  --shards=16 \
  --query-threads=8 \
  --commit-interval=60 \
  --cache-size=10000 \
  --enable-hnsw=true \
  --optimization=3 \
  --meta-dir=./metadata \
  --enable-pq=true

python3 ./db.py
streamlit run main.py
```

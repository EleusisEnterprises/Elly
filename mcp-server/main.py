import os

import openai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

openai.api_key = os.environ.get("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    """Forward the message to OpenAI and return its reply."""
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": request.message}],
    )
    answer = completion.choices[0].message["content"]
    return {"response": answer}

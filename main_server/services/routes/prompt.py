import os
import httpx
from pydantic import BaseModel
from fastapi import FastAPI

prompt_app = FastAPI()

class FeedbackData(BaseModel):
    prompt: str

async def generate_prompt_response(prompt_message):
    print("prompt message is", prompt_message)
    url = os.environ.get("PROMPT_SERVER_ADDRESS", "http://localhost:11434/api/generate")

    payload = {
        "model": "llama2",
        "prompt": f"{prompt_message}",
        "stream": False
    }

    timeout = httpx.Timeout(50.0)  

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=timeout)
        print("raw response",response)
        return response.json()

@prompt_app.post("/get_feedback")
async def handle_get_feedback(data: FeedbackData):
    response = await generate_prompt_response(data.prompt)
    print("response is",response)
    return {"feedback_response": response["response"]}

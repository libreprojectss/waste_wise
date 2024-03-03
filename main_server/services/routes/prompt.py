import os
import httpx
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from models.prompt import PromptData
from config.connect_db import connect_db
import random
import threading, asyncio

prompt_app = FastAPI()

class FeedbackData(BaseModel):
    prompt: str

async def generate_prompt_response(request_key,request_type,db: Session):
    prompt_message=f"how to {request_type} {request_key} ?"
    print("prompt message is", prompt_message)
    url = os.environ.get("PROMPT_SERVER_ADDRESS", "http://localhost:11434/api/generate")

    payload = {
        "model": "llama2",
        "prompt": f"{prompt_message}",
        "stream": False
    }

    timeout = httpx.Timeout(500.0)  

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=timeout)
        print(response)
        db_prompt_data = PromptData(
            request_key=request_key,
            request_type=request_type,
            result=response.json()["response"],
            )
        db.add(db_prompt_data)
        db.commit()
        return response.json()["response"]



class PromptDataCreate(BaseModel):
    request_key: str
    request_type: str
    result:str=None

@prompt_app.post("/prompt_data/")
async def create_prompt_data(request: Request, db: Session = Depends(connect_db)):
    try:
       

        prompt_data_dict = await request.json()
        prompt_data = PromptDataCreate(**prompt_data_dict)
        result = db.query(PromptData).filter(
        PromptData.request_key == prompt_data.request_key,
        PromptData.request_type == prompt_data.request_type
    ).all() 
        if len(result)==0:
            response = await generate_prompt_response(prompt_data.request_key, prompt_data.request_type, db)
            prompt_data.result = response
            db_prompt_data = PromptData(**prompt_data.dict())
            db.add(db_prompt_data)
            db.commit()
            db.refresh(db_prompt_data)
            result=response
        else:
            random_index = random.randrange(len(result))
            prompt_data = result[random_index]
            def background_task():
                asyncio.run(generate_prompt_response(prompt_data.request_key, prompt_data.request_type, db))

            background_thread = threading.Thread(target=background_task)
            background_thread.start()
        return {"result": prompt_data}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


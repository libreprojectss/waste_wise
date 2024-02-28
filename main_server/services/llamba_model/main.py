from fastapi import FastAPI

app = FastAPI()

# @app.post("/get_feedback")
# async def handle_get_feedback(data: dict):
#     feedback_response=await 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

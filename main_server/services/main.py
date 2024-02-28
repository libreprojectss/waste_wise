from fastapi import FastAPI
from routes.prompt import prompt_app

app = FastAPI()

app.mount("/api", app=prompt_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

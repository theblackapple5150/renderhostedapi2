from fastapi import FastAPI
import os, uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=True,
    )

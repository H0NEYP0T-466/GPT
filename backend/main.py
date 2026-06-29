from fastapi import FastAPI
import uvicorn
import logging
from module.bigramModel import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app=FastAPI()

@app.get("/generate")
def generate():
    return random()

if __name__ == "__main__":
    
    logger.info("hey")
    uvicorn.run(
        "main:app",
        port=8010,
        reload=True,
    )


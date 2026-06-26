from fastapi import FastAPI
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app=FastAPI()

@app.get("/")
def fun():
    return "hello world"

if __name__ == "__main__":
    
    logger.info("hey")
    uvicorn.run(
        "main:app",
        port=8010,
        reload=True,
    )


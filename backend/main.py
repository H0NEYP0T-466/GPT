from fastapi import FastAPI
import uvicorn
import logging
from config.preprocessing import data_Reading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app=FastAPI()

@app.get("/")
def fun():
    num=data_Reading()
    return f"dataset size is: {num}"

if __name__ == "__main__":
    
    logger.info("hey")
    uvicorn.run(
        "main:app",
        port=8010,
        reload=True,
    )


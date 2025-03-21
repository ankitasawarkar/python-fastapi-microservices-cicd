from fastapi import FastAPI
import uvicorn
from mylib.logic import (wiki as wiki_summary, search_wiki)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello All! Look at Wikipedia APIs."}

@app.get("/search/{value}")
async def search(value: str):
    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{value}")
async def wiki(value: str):
    result = wiki_summary(value)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8088, host='0.0.0.0') 
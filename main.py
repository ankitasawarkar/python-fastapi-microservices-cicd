from fastapi import FastAPI
import uvicorn
from mylib.logic import (wiki as wiki_summary, search_wiki, phrase_wiki)
# from mylib.nlp_model import (user_Document, find_similarity)

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

    
@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and return phrases"""

    result = phrase_wiki(name)
    return {"result": result}


# @app.get("/document/similarity/{query}")
# async def find_query_similarity(document: str, query: str):
#     result = find_similarity(document, query)
#     return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8091, host='0.0.0.0') 
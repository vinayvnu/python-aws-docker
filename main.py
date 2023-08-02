from mylib.logic import wiki as wiki_logic, search_wiki, phrases as wiki_phrases
from fastapi import FastAPI
import uvicorn

app = FastAPI()
app.get("/")
async def root():
    return {"message": "wikipedia API. Call /search or /wiki"}

@app.get("/search/{value}")
async def search(value: str):
    '''page to search in wikipedia'''
    return {"results": search_wiki(value)}

@app.get("/wiki/{name}")
async def wiki(name: str):
    '''retrives wikipedia page'''
    return {"results": wiki_logic(name)}

@app.get("/phrase/{name}")
async def phrase(name: str):
    '''retrives wikipedia page and return phrases'''
    return {"results": wiki_phrases(name)}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')


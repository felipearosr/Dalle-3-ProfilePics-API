from openai import OpenAI
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/openai")
def openai():
    return {"Hello": "OpenAI"}

def createImage():
    client = OpenAI()

    response = client.images.generate(

    )

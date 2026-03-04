from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Olá MUNDO Começamos com o Git"}

@app.get("/teste1")
async def funcaoteste():
    return {"message": "Deu certo o teste nº 02"}
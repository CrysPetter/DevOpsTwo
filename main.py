from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
<<<<<<< Updated upstream
    return {"message": "Olá MUNDO Começamos com o Git"}
=======
    return {"message": "Olá MUNDO Começamos com o Git"}

@app.get("/teste1")
async def funcaoteste():
    return {"message": "Deu certo o teste nº 02"}

@app.get("/teste2")
async def funcaoteste2():
    return {"teste2": True, "num_aleatorio": random.randint(0, 1000)}
>>>>>>> Stashed changes

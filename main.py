from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Olá MUNDO Começamos com o Git"}

# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"message": "Deu certo o teste nº 02"}

# http://127.0.0.1:8000/teste2
@app.get("/teste2")
async def funcaoteste2():
    return {"teste2": True, "num_aleatorio": random.randint(0, 1000)}

# http://127.0.0.1:8000/teste3
@app.get("/teste3")
async def funcaoteste3():
    return {"teste3": True, "num_aleatorio": random.randint(0, 500000)}

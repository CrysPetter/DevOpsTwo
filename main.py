from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Olá MUNDO Começamos com o Git"}
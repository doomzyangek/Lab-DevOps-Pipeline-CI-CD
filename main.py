from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Testando Ambiente de Homologacao na porta 8080"}

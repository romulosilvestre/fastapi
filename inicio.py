from fastapi import FastAPI,HTTPException,status

app = FastAPI()

# rota index
# programação assíncrona

@app.get("/")
async def index():
    return {"mensagem":"Olá mundo!"}


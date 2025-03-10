from fastapi import FastAPI
from database import engine, Base
from app.routers import funcionario_router, cliente_router, produto_router

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir rotas
app.include_router(funcionario_router.router)
app.include_router(cliente_router.router)
app.include_router(produto_router.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

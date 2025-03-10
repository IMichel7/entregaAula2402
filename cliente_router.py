from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.crud.cliente_crud import *

router = APIRouter()

@router.post("/cliente/")
def create(nome: str, cpf: str, telefone: str, db: Session = Depends(get_db)):
    return create_cliente(db, nome, cpf, telefone)

@router.get("/cliente/")
def read(db: Session = Depends(get_db)):
    return get_clientes(db)

@router.put("/cliente/{id}")
def update(id: int, nome: str, telefone: str, db: Session = Depends(get_db)):
    return update_cliente(db, id, nome, telefone)

@router.delete("/cliente/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return delete_cliente(db, id)

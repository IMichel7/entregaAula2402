from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.crud.produto_crud import *

router = APIRouter()

@router.post("/produto/")
def create(nome: str, preco: int, db: Session = Depends(get_db)):
    return create_produto(db, nome, preco)

@router.get("/produto/")
def read(db: Session = Depends(get_db)):
    return get_produtos(db)

@router.put("/produto/{id}")
def update(id: int, nome: str, preco: int, db: Session = Depends(get_db)):
    return update_produto(db, id, nome, preco)

@router.delete("/produto/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return delete_produto(db, id)

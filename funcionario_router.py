from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from database import get_db
from app.crud.funcionario_crud import *

router = APIRouter()

@router.post("/funcionario/")
def create(nome: str, matricula: str, cpf: str, telefone: str, db: Session = Depends(get_db)):
    return create_funcionario(db, nome, matricula, cpf, telefone)

@router.put("/funcionario/{id}")
def update(id: int, nome: str, telefone: str, db: Session = Depends(get_db)):
    return update_funcionario(db, id, nome, telefone)

@router.get("/funcionario/")
def read(db: Session = Depends(get_db)):
    return get_funcionarios(db)


@router.delete("/funcionario/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return delete_funcionario(db, id)

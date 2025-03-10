from sqlalchemy.orm import Session
from app.models.funcionario import Funcionario

def create_funcionario(db: Session, nome: str, matricula: str, cpf: str, telefone: str):
    funcionario = Funcionario(nome=nome, matricula=matricula, cpf=cpf, telefone=telefone)
    db.add(funcionario)
    db.commit()
    db.refresh(funcionario)
    return funcionario

def get_funcionarios(db: Session):
    return db.query(Funcionario).all()

def update_funcionario(db: Session, id: int, nome: str, telefone: str):
    funcionario = db.query(Funcionario).filter(Funcionario.id == id).first()
    if funcionario:
        funcionario.nome = nome
        funcionario.telefone = telefone
        db.commit()
    return funcionario

def delete_funcionario(db: Session, id: int):
    funcionario = db.query(Funcionario).filter(Funcionario.id == id).first()
    if funcionario:
        db.delete(funcionario)
        db.commit()
    return funcionario

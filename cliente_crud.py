from sqlalchemy.orm import Session
from app.models.cliente import Cliente

def create_cliente(db: Session, nome: str, cpf: str, telefone: str):
    cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def get_clientes(db: Session):
    return db.query(Cliente).all()

def update_cliente(db: Session, id: int, nome: str, telefone: str):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if cliente:
        cliente.nome = nome
        cliente.telefone = telefone
        db.commit()
    return cliente

def delete_cliente(db: Session, id: int):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente

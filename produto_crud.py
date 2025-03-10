from sqlalchemy.orm import Session
from app.models.produto import Produto

def create_produto(db: Session, nome: str, preco: int):
    produto = Produto(nome=nome, preco=preco)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

def get_produtos(db: Session):
    return db.query(Produto).all()

def update_produto(db: Session, id: int, nome: str, preco: int):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        produto.nome = nome
        produto.preco = preco
        db.commit()
    return produto

def delete_produto(db: Session, id: int):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return produto

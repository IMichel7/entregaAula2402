from sqlalchemy import Column, Integer, String
from database import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    matricula = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String)

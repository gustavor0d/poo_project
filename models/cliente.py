from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    idCliente = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    telefone = Column(String)
    pedidos = relationship("Pedido", back_populates="cliente")

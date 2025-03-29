from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Sabor(Base):
    __tablename__ = 'sabor'

    idSabor = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    sorveteria_id = Column(Integer, ForeignKey('sorveteria.idSorveteria'))
    sorveteria = relationship("Sorveteria", back_populates="sabores")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class Sorveteria(Base):
    __tablename__ = 'sorveteria'

    idSorveteria = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    sabores = relationship("Sabor", back_populates="sorveteria")

    def adicionar_sabor(self, sabor):
        self.sabores.append(sabor)

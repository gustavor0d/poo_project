from sqlalchemy import Column, Integer, Float, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from models.base import Base

pedido_sabor = Table('pedido_sabor', Base.metadata,
    Column('pedido_id', Integer, ForeignKey('pedido.idPedido')),
    Column('sabor_id', Integer, ForeignKey('sabor.idSabor'))
)

class Pedido(Base):
    __tablename__ = 'pedido'

    idPedido = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.idCliente'))
    cliente = relationship("Cliente", back_populates="pedidos")
    sabores = relationship("Sabor", secondary=pedido_sabor)
    total = Column(Float)
    data = Column(Date)

    def calcular_total(self):
        self.total = sum(sabor.preco for sabor in self.sabores)

    def atribuir_data(self, today):
        self.data = today

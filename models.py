from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)

    weapons = relationship("Weapon", back_populates="supplier")

class Warehouse(Base):
    __tablename__ = "warehouses"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)

    weapons = relationship("Weapon", back_populates="warehouse")

class Weapon(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    warehouse = relationship("Warehouse", back_populates="weapons")
    supplier = relationship("Supplier", back_populates="weapons")


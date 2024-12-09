from pydantic import BaseModel
from typing import Optional

class SupplierBase(BaseModel):
    name: str
    contact_info: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True

class WarehouseBase(BaseModel):
    location: str

class WarehouseCreate(WarehouseBase):
    pass

class Warehouse(WarehouseBase):
    id: int

    class Config:
        orm_mode = True

class WeaponBase(BaseModel):
    name: str
    type: str
    quantity: float
    warehouse_id: int
    supplier_id: int

class WeaponCreate(WeaponBase):
    pass

class Weapon(WeaponBase):
    id: int

    class Config:
        orm_mode = True


from typing import Optional
from pydantic import BaseModel


class SupplierBase(BaseModel):
    name: str
    contact_info: Optional[str] = None

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True

class WarehouseBase(BaseModel):
    location: str

class Warehouse(WarehouseBase):
    id: int

    class Config:
        orm_mode = True

class WeaponBase(BaseModel):
    name: str
    type: str
    quantity: float

class WeaponWithRelations(WeaponBase):
    id: int
    warehouse: Warehouse
    supplier: Supplier

    class Config:
        orm_mode = True

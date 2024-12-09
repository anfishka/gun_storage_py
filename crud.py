from sqlalchemy.orm import Session
from models import Supplier, Warehouse, Weapon
from schemas import SupplierCreate, WarehouseCreate, WeaponCreate
from fastapi import HTTPException

######################### suppliers #################################

def create_supplier(db: Session, supplier: SupplierCreate):
    db_supplier = Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_supplier_by_id(db: Session, supplier_id: int):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail=f"Supplier with id {supplier_id} not found")
    return supplier

def get_all_suppliers(db: Session):
    return db.query(Supplier).all()

def delete_supplier(db: Session, supplier_id: int):
    supplier = get_supplier_by_id(db, supplier_id)
    db.delete(supplier)
    db.commit()
    return {"message": f"Supplier with id {supplier_id} deleted successfully"}

######################### warehouse #################################

def create_warehouse(db: Session, warehouse: WarehouseCreate):
    db_warehouse = Warehouse(**warehouse.dict())
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse

def get_warehouse_by_id(db: Session, warehouse_id: int):
    warehouse = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404, detail=f"Warehouse with id {warehouse_id} not found")
    return warehouse

def get_all_warehouses(db: Session):
    return db.query(Warehouse).all()

def delete_warehouse(db: Session, warehouse_id: int):
    warehouse = get_warehouse_by_id(db, warehouse_id)
    db.delete(warehouse)
    db.commit()
    return {"message": f"Warehouse with id {warehouse_id} deleted successfully"}

######################### weapon #################################

def create_weapon(db: Session, weapon: WeaponCreate):
    db_weapon = Weapon(**weapon.dict())
    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)
    return db_weapon

def get_weapon_by_id(db: Session, weapon_id: int):
    weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail=f"Weapon with id {weapon_id} not found")
    return weapon

def get_all_weapons(db: Session):
    return db.query(Weapon).all()

def delete_weapon(db: Session, weapon_id: int):
    weapon = get_weapon_by_id(db, weapon_id)
    db.delete(weapon)
    db.commit()
    return {"message": f"Weapon with id {weapon_id} deleted successfully"}

def update_weapon_partially(db: Session, weapon_id: int, updates: dict):
    weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail=f"Weapon with id {weapon_id} not found")

    for key, value in updates.items():
        if value and value.lower() == "string":
            continue
        if hasattr(weapon, key):
            setattr(weapon, key, value)

    db.commit()
    db.refresh(weapon)
    return weapon

def get_all_weapons_with_relations(db: Session):
    weapons = db.query(Weapon).all()
    return weapons

def get_weapon_with_relations(db: Session, weapon_id: int):
    weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail=f"Weapon with id {weapon_id} not found")
    return weapon

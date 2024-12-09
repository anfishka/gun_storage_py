from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from schemas import SupplierCreate, WarehouseCreate, WeaponCreate
from crud import (
    create_supplier, get_all_suppliers, get_supplier_by_id, delete_supplier,
    create_warehouse, get_all_warehouses, get_warehouse_by_id, delete_warehouse,
    create_weapon, get_all_weapons, get_weapon_by_id, delete_weapon,
    update_weapon_partially, get_all_weapons_with_relations, get_weapon_with_relations
)
from schemas import WeaponWithRelations


Base.metadata.create_all(bind=engine)

app = FastAPI()

######################### suppliers #################################

@app.get("/suppliers/")
def list_suppliers(db: Session = Depends(get_db)):
    return get_all_suppliers(db)

@app.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    return get_supplier_by_id(db, supplier_id)

@app.post("/suppliers/")
def add_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    return create_supplier(db, supplier)

@app.delete("/suppliers/{supplier_id}")
def delete_supplier_route(supplier_id: int, db: Session = Depends(get_db)):
    return delete_supplier(db, supplier_id)

######################### warehouses #################################

@app.get("/warehouses/")
def list_warehouses(db: Session = Depends(get_db)):
    return get_all_warehouses(db)

@app.get("/warehouses/{warehouse_id}")
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    return get_warehouse_by_id(db, warehouse_id)

@app.post("/warehouses/")
def add_warehouse(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    return create_warehouse(db, warehouse)

@app.delete("/warehouses/{warehouse_id}")
def delete_warehouse_route(warehouse_id: int, db: Session = Depends(get_db)):
    return delete_warehouse(db, warehouse_id)

######################### weapons #################################

@app.get("/weapons/", response_model=list[WeaponWithRelations])
def list_weapons_with_relations(db: Session = Depends(get_db)):
    return get_all_weapons_with_relations(db)

@app.get("/weapons/{weapon_id}", response_model=WeaponWithRelations)
def get_weapon_with_relations_route(weapon_id: int, db: Session = Depends(get_db)):
    return get_weapon_with_relations(db, weapon_id)

@app.post("/weapons/")
def add_weapon(weapon: WeaponCreate, db: Session = Depends(get_db)):
    return create_weapon(db, weapon)

@app.patch("/weapons/{weapon_id}")
def patch_weapon(weapon_id: int, updates: dict, db: Session = Depends(get_db)):
    return update_weapon_partially(db, weapon_id, updates)

@app.delete("/weapons/{weapon_id}")
def delete_weapon_route(weapon_id: int, db: Session = Depends(get_db)):
    return delete_weapon(db, weapon_id)






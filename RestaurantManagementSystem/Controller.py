# Task Two:
# The first API is (getAPI) /getMenu (which will get the menu and return it)        (use what was written in display menu written)
# The second API is (post API) /createMenu (which will help insert the values into the columns for menu)
# The third API is (update API) /updateValue (which will update the value in the menu using the input in the URL)
# EX for third API: menu/itemId/*name=*something* or price=*something*
# NOTE: API MAKING THING GOES HERE

from fastapi import FastAPI, Depends, HTTPException
from Model import sessionLocal, menu
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()
def getdb():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class menuItemCreate(BaseModel):
    item_id : int
    name : str
    price : float

class menuItemUpdate(BaseModel):
    item_id: int
    name: str | None = None
    price: float | None = None

@app.get("/getMenu")
def get_menu(db: Session=Depends(getdb)):
    menu_items = db.query(menu).all()
    return {"Menu": menu_items}

@app.post("/createMenu")
def create_menu(item: menuItemCreate, db: Session=Depends(getdb)):
    existingitem = db.query(menu).filter(menu.itemId==item.item_id).first()
    if existingitem:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    newitem = menu(itemId = item.item_id, itemName = item.name, itemPrice = item.price)
    db.add(newitem)
    db.commit()
    # db.refresh(newitem)
    return {"message": "Item added successfully", "menu": menu}


@app.put("/updateValue")
def update_menu(item: menuItemUpdate, db: Session = Depends(getdb)):
    existing_item = db.query(menu).filter(menu.itemId == item.item_id).first()
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.name is None and item.price is None:
        raise HTTPException(status_code=400, detail="No values provided for update")
    if item.name is not None:
        existing_item.itemName = item.name
    if item.price is not None:
        existing_item.itemPrice = item.price
    db.commit()
    db.refresh(existing_item)
    return {"message": "Item updated successfully", "menu": existing_item}


# HIRE is POST API


# FIRE is DELETE API

# TASK ONE: -DONE
# Fix update_menu according to create_menu (since db was added and everything)
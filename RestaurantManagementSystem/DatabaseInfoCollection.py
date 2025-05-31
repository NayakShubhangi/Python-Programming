from Model import session

db = session
menu_items = db.query(menu).all()
Names = [item.itemName for item in menu_items]
Prices = [item.itemPrice for item in menu_items]


# Bill generation and other things go here...
# Write the code to generate a bill:
# 1. Take input from user (name and everything) 
# 2. Add details to database
# 3. Ask user for food items they would like to purchase
# 4. Access prices for all the wanted food items
# 5. Add together their prices and total the bill
# 6. If any discounts, apply discounts to bill
# 7. Show customer their final bill, using Pandas

# Create class called restaurant billing, which should have the methods: display menu, take order, and generate bill
# For display menu, the parameter is menu_items (where the menu items are stored in as a dictionary with ID, name, and price) use
# a for loop to iterate through and show everything

# For take order, initialize a new dictionary called ordered_items (where the ordered items are stored in a dictionary with the name of the item
# as the key, and the value would be a tuple, where the tuple's first value would be the price of the item, and the second value would be the
# quantity of the item)
# Two input statements, the first asks for id of the item, the second asks for the quantity, (WHILE USER DOES NOT WRITE DONE KEYWORD)
# Check whether the item.id exists in the menu_items, and if it does exist, then add the item.name, item.price, and quantity to ordered_items

# For generate bill, do steps 4-7

from Model import session, menu, customers, membership_card, admin, discounts
from sqlalchemy import update, insert
import pandas
import hashlib
import logging
import datetime as dt
import pyttsx3


class restaurantBilling:
    def __init__(self):
        self.db = session
        logging.basicConfig(level=logging.INFO)
        self.speakText("Welcome to the restaurant!")
        logging.info("Welcome to the restaurant!")
        # (DONE) this goes in audio speech now

    # TASK FOUR:
    # Need a method/function that can take a parameter String. The parameter is a password, and then the method/function should return the
    # string conversion of the hashed version of the password. (Hashed version should be stored in the database,
    # while the string conversion doesn't really do anything)
    # NOTE: CODE GOES HERE
    def speakText(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


    def takeInput(self):
        """
        Takes customer's information and returns it

        Parameters:
        None

        Returns:
        String and Integer: The customer's name and the customer's mobile number
        """
        customer_name = input("Enter you name: ")
        customer_mobileNumber = int(input("Enter your mobile number: "))
        return customer_name, customer_mobileNumber
    
    def encryptPassword(self, password: str):
        """
        Takes a password and encrypts it

        Parameters:
        password (str): The password that will be encrypted

        Returns:
        String: The encrypted password
        """
        encodedPassword = password.encode('utf-8')
        hashedPassword = hashlib.sha256(encodedPassword)
        return hashedPassword.hexdigest()

    def displayMenu(self):
        """
        Displays the menu

        Parameters:
        None

        Returns:
        A list of menu_items.
        """
        menu_items = self.db.query(menu).all()
        Ids = [item.itemId for item in menu_items]
        Names = [item.itemName for item in menu_items]
        Prices = [item.itemPrice for item in menu_items]
        df = pandas.DataFrame({"ID": Ids, "Name": Names, "Price": Prices})
        logging.info("---------- Menu ----------")
        logging.info(df.to_string(index=False))
        return Names, Prices
        
    def takeOrder(self):
        """
        Takes the customer's order

        Parameters:
        None

        Returns:
        Dictionary: The menu items that the customer ordered
        """
        ordered_items = {}
        while True:
            item_id = input("Enter the ID of the item to order, use the 'done' keyword to finish if you are done ordering: ")
            if item_id.lower() == "done":
                break
            item = self.db.query(menu).filter(menu.itemId == int(item_id)).first()
            if item:
                quantity = int(input("Enter the quantity of the item you would like to order: "))
                ordered_items[item.itemName] = (item.itemPrice, quantity)
            else:
                logging.error("The item does not exist...")
        return ordered_items

    def discountEligibility(self):
        """
        Checks if the customer is eligible for any extra discount

        Parameters:
        None

        Returns:
        A tuple which consists of two values:
            customerRole (str): The role the customer had which made them eligible for any extra discount (empty if none).
            roleDiscount (int): The extra discount the customer is eligible for (0 if none).
        A list of roles.
        """
        logging.info("Based on your role, you may be eligible for an extra discount. (EX: Student)")
        customerRole = input("Enter your role (Leave empty if none): ")
        applicableRoles = self.db.query(discounts).all()
        roleDiscounts = applicableRoles.discount
        if customerRole:
            roleExists = self.db.query(discounts).filter(discounts.role == customerRole.lower()).first()
            roleDiscount = roleExists.discount
            if roleDiscount:
                return (customerRole, roleDiscount), applicableRoles, roleDiscounts
        else:
            roleDiscount = 0
        return (0, 0)
        # (SHIFTED) TASK TWO:
        # make ONE function that could be repurposed for all of them
        # ASK IF THEY HAVE SOME KIND OF ROLE     *decide where it should be put*-> BEFORE BILL GENERATION
        # if they say that they are a *placeholder*:
        #      - Apply additional *some*% discount based on whether they are in the database
        
        # EXAMPLE
        # if customer is a student:
        #     - Apply additional 10% discount

    def generateBill(self, ordered_items, memcard, roleInfo):
        """
        Generates the customer's bill

        Parameters:
        ordered_items (dict): The items that the customer ordered
        memcard (tuple): Has two values, both of which are integers:
                    First value represents the type of card the user has renewed/bought (0 if none was purchased),
                    Second value represents the cost of the card (0 if none was purchased),
                    Third value represents whether the customer would like to use their card (if they have one)
        role_discount (tuple): Has two values:
                    First value (str): The customer's role (if they had one that was eligible),
                    Second value (int): The extra discount that customers may or may not get (from discountEligibility())

        Returns:
        None
        """
        # TASK ONE (DONE):
        # REALIZATION
        # Just realized, but we don't actually add any discounts from the membership card; just the normal discount for all customers
        # REMOVED NORMAL DISCOUNT- replace it with the membership card discount if any
        customer_role = roleInfo[0]
        role_discount = roleInfo[1]
        typeCard = memcard[0]
        priceCard = memcard[1]
        useCard = memcard[2]
        membershipCard = self.db.query(membership_card).filter(membership_card.cardType == customers.membershipCard).first()
        discountOfCard = membershipCard.discountAdded
        total_price = 0
        for price, quantity in ordered_items.values():
            total_price += price * quantity
        card_discount_amount = total_price * (discountOfCard / 100)
        role_discount_amount = total_price * (role_discount / 100)
        grand_total = total_price - role_discount_amount - card_discount_amount + priceCard
        bill_series = pandas.Series()
        if useCard:
            memDiscount_series = pandas.Series({
                f"Membership Card Discount": f"{discountOfCard}%"
            })
            bill_series = pandas.concat([bill_series, memDiscount_series])
        if role_discount:
            roleDiscount_series = pandas.Series({
                f"{customer_role}'s Discount": f"{role_discount}%"
            })
            bill_series = pandas.concat([bill_series, roleDiscount_series])
        if priceCard:
            card_series = pandas.Series({
                "Card Purchased": f"Type {typeCard}",
                "Card Price": priceCard
            })
            bill_series = pandas.concat([bill_series, card_series])
        grand_total_series = pandas.Series({
            "Grand Total": grand_total
        })
        bill_series = pandas.concat([bill_series, grand_total_series])
        bill_data = {
            "Item Name": [],
            "Quantity": [],
            "Unit Price": [],
            "Total Price": []
        }
        for item_name, (item_price, item_quantity) in ordered_items.items():
            bill_data["Item Name"].append(item_name)
            bill_data["Quantity"].append(item_quantity)
            bill_data["Unit Price"].append(item_price)
            bill_data["Total Price"].append(item_quantity * item_price)
        bill_df = pandas.DataFrame(bill_data)
        logging.info("\n---------- Bill ----------")
        logging.info(bill_df)
        print("\n", bill_series)
        
    def validateMembership(self, customerName):
        """
        Checks whether the customer has membership or not, valid or not

        Parameters:
        customerName (str): The customer's name

        Returns:
        Tuple: (Integer: Card Type of Customer's Membership Card (0 If They Don't Have One),
                Float: Price of Membership Card Bought (0 If None was Purchased),
                Bool: Whether the customer is using their Membership Card or not)
        """
        haveMembership = input("Do you have a membership card? Answer with 'yes' or 'no': ")
        customer = self.db.query(customers).filter(customers.name == customerName).first()
        # TODO ERROR: AttributeError: NoneType object has no attribute membershipCard
        # Probably because the first time, customer doesn't exist in database, so NoneType appears
        card = self.db.query(membership_card).filter(membership_card.cardType == customer.membershipCard).first()
        if haveMembership.lower() == 'yes':
            if customer and customer.membershipCard:
                if customer.cardVisits < card.cardMaximumVisits:
                    extraDiscount = card.discountAdded
                    useMembership = input(f"Would you like to use your membership card and get an extra {extraDiscount}% off your order? (Yes/No): ")
                    if useMembership.lower() == 'yes':
                        self.db.execute(update(customers).where(customers.name == customerName).values(cardVisits=customer.cardVisits + 1))
                        self.db.commit()
                        cardSelect = self.db.query(membership_card).filter(membership_card.cardType == customer.membershipCard).first()
                        typeofCard = cardSelect.cardType
                        return (typeofCard, float(0), True)
                    cardSelect = self.db.query(membership_card).filter(membership_card.cardType == customer.membershipCard).first()
                    typeofCard = cardSelect.cardType
                    return (typeofCard, float(0), False)
                else:
                    renew = input("Your membership has reached the maximum number of visits. Would you like to renew it? (Yes/No): ")
                    if renew.lower() == 'yes':
                        self.db.execute(update(customers).where(customers.name == customerName).values(cardVisits=0))
                        self.db.commit()
                        cardtoRenew = self.db.query(membership_card).filter(membership_card.cardType == customer.membershipCard).first()
                        memcardPrice = cardtoRenew.cardPrice
                        useMembership = input(f"Would you like to use your membership card and get an extra {extraDiscount}% off your order? (Yes/No): ")
                        if useMembership.lower() == 'yes':
                            self.db.execute(update(customers).where(customers.name == customerName).values(cardVisits=customer.cardVisits + 1))
                            self.db.commit()
                            cardSelect = self.db.query(membership_card).filter(membership_card.cardType == customer.membershipCard).first()
                            typeofCard = cardSelect.cardType
                            return (int(customer.membershipCard), float(memcardPrice), True)
                        return (int(customer.membershipCard), float(memcardPrice), False)
                    else:
                        self.db.execute(update(customers).where(customers.name == customerName).values(membershipCard=False, cardVisits=0))
                        self.db.commit()
                        return (0, float(0), False)
            else:
                logging.error("You do not have a valid membership card on record.")
                return (0, float(0), False)
        else:
            cards_available = self.db.query(membership_card).all()
            Types = [card.cardType for card in cards_available]
            Prices = [card.cardPrice for card in cards_available]
            ExtraDiscs = [card.discountAdded for card in cards_available]
            MaxVisits = [card.cardMaximumVisits for card in cards_available]
            card_data = {
                "Card Type": [],
                "Card Price": [],
                "Extra Discount (%)": [],
                "Maximum Visits": []
            }
            for type in Types:
                card_data["Card Type"].append(type)
            for price in Prices:
                card_data["Card Price"].append(price)
            for extradisc in ExtraDiscs:
                card_data["Extra Discount (%)"].append(extradisc)
            for maxvisit in MaxVisits:
                card_data["Maximum Visits"].append(maxvisit)
            card_df = pandas.DataFrame(card_data)
            logging.info("\nMembership Cards")
            logging.info(card_df)
            wantMembership = input("Would you like to purchase membership card? (Yes/No): ")
            if wantMembership.lower() == 'yes':
                typeWanted = int(input("Enter the card type you would like to purchase: "))
                cardWanted = self.db.query(membershipcard).filter(membershipcard.cardType == typeWanted)
                extraDiscount = cardWanted.discountAdded
                self.db.execute(update(customers).where(customers.name == customerName).values(membershipCard=typeWanted, cardVisits=0))
                self.db.commit()
                useMembership = input(f"Would you like to use your membership card and get an extra {extraDiscount}% off your order? (Yes/No): ")
                if useMembership.lower() == 'yes':
                    self.db.execute(update(customers).where(customers.name == customerName).values(cardVisits=customer.cardVisits + 1))
                    # TODO ERROR: Apparently, customer is NoneType and doesn't have an attribute cardVisits
                    # FIGURED IT OUT: The first time a customer goes to the restaurant, they don't exist in the database,
                    # and they aren't added until the end of the program, so the customer doesn't actually exsist according to
                    # the database. As a result, it's none, which then throws an error.
                    # Probably just move the "updating" stuff to the info insertion section,
                    # and just return the information that's needed, since this function is run directly in that function
                    self.db.commit()
                cardtoRenew = self.db.query(membershipcard).filter(membershipcard.cardType == customer.membershipCard)
                memcardPrice = cardtoRenew.cardPrice
                return (typeWanted, float(memcardPrice))
            else:
                return (0, float(0))

    def paymentVerification(self):
        """
        Checks what payment method the customer chooses

        Parameters:
        None

        Returns:
        Str: What payment method the customer chose
        """
        logging.info("Enter your payment method. Your options are:")
        logging.info("Press 1 for Credit Card")
        logging.info("Press 2 for Debit Card")
        logging.info("Press 3 for Cash")
        payment_method_type = int(input("Enter your payment method (Press 1, 2, or 3): "))
        match payment_method_type:
            case 1:
                payment_method = "Credit Card"
            case 2:
                payment_method = "Debit Card"
            case 3:
                payment_method = "Cash"
        return payment_method
    
    # TODO:
    # def generateReceipt(self, ...)

    def customerInfoInsertion(self, name, number, paymethod, memcard):
        """
        Inserts the customer's information into the database

        Parameters:
        name (Str): The customer's name
        number (Int): The customer's mobile number
        paymethod (Str): The customer's chosen payment method
        memcard (Bool): Whether the customer has a membership card

        Returns:
        None
        """
        
        customer = self.db.query(customers).filter(customers.name == name, customers.mobileNumber == number).first()
        year, month, day = customer.firstVisit.split("-")
        # TODO ERROR: visitSet = customer.cardVisits + 1 (AttributeError: 'NoneType' object has no attribute 'cardVisits)
        
        # FIGURED IT OUT: When a customer first goes to the restaurant, they don't exist in the database, and they're added
        # in this portion, so trying to find them when they don't really exist will just return a NoneType
        if customer:
            if memcard:
                visitsSet = customer.cardVisits
            else:
                visitsSet = 0
            if dt.date.today() > dt.date(int(year), int(month), int(day)):
                self.db.execute(update(customers).where(customers.currentVisit).values(currentVisit=dt.date.today()))
                # TODO ERROR: [SQL: UPDATE `Customers` SET `currentVisit`=%(currentVisit)s WHERE `Customers`.`currentVisit`]
                # [parameters: {'currentVisit': datetime.date(2025, 4, 19)}]
                # (Background on this error at: https://sqlalche.me/e/20/e3q8)
            self.db.execute(update(customers).where(customers.name == customer.name).values(paymentMethod=paymethod))
            self.db.execute(update(customers).where(customers.name == customer.name).values(cardVisits=visitsSet))
            self.db.commit()
        if not customer:
            if memcard == False:
                visitsSet = 0
            else:
                visitSet = customer.cardVisits + 1
            self.db.execute(insert(customers).values(
                name = name,
                mobileNumber = number,
                paymentMethod = paymethod,
                firstVisit = today,
                currentVisit = today,
                membershipCard = memcard,
                cardVisits = 0
            ))
            self.db.commit()

def databaseInfoCollection():
    db = session
    menu_thing = db.query(menu).all()
    Names = [item.itemName for item in menu_thing]
    Prices = [item.itemPrice for item in menu_thing]
    menu_items = {}
    for itemindex in range(len(Names)):
        menu_items[Names[itemindex]] = Prices[itemindex]
    
    applicableRoles = db.query(discounts).all()
    roles = [role.role for role in applicableRoles]
    discounts_possible = [role.discount for role in applicableRoles]
    role_information = {}
    for itemindex in range(len(roles)):
        role_information[roles[itemindex]] = discounts_possible[itemindex]

    # cards_available = db.query(membership_card).all()
    # Types = [card.cardType for card in cards_available]
    # Prices = [card.cardPrice for card in cards_available]
    # ExtraDiscs = [card.discountAdded for card in cards_available]
    # MaxVisits = [card.cardMaximumVisits for card in cards_available]

    return menu_items, role_information

if __name__ == "__main__":
    # TASK TWO (DONE):
    # Figure out a way to see how to arrange this in streamlit
    restaurant = restaurantBilling()
    name, number = restaurant.takeInput()                              # Input boxes
    menu_names, menu_prices = restaurant.displayMenu()                 # Organize in a vertical rectangular style- like real menus
    ordered_things = restaurant.takeOrder()                            # Checkboxes next to items- if selected, show input box for quantity
    memcard = restaurant.validateMembership(name)                      # Input box/Checkboxes, with appropriate response messages
    roleInfo, applicableRoles = restaurant.discountEligibility()       # Checkboxes maybe?
    restaurant.generateBill(ordered_things, memcard, roleInfo)         # Organize in a vertical rectangle- like a receipt
    paymethod = restaurant.paymentVerification()                       # Three options- perhaps buttons?
    restaurant.customerInfoInsertion(name, number, paymethod, memcard)
    restaurant.speakText(f"Thank you, {name}! Please come again!")
    # (DONE) thank you stuff is here

    # TASK THREE (DONE):
    # Gather three (colorful) images to use for the restaurant? (1 is welcome message img, other 2 go wherever)

    # TASK FOUR (DONE):
    # Change the two admin names to "Shubhangi" and "Harshith"
    # Change the two staff names to Staff1 and Staff2

# TASK ONE is in Controller.py

# TASK TWO: Done
# Use series or dataframe to display the menu in displayMenu.

# TASK THREE: Done
# See which is better: Pass the ordered_items as a parameter, or not using it as a parameter.

# TASK FOUR:
# Brush up on walrus operator, pandas.

# TASK FIVE:
# Figure out what to do next for this project, and prepare on how to do it.
# Add customer information to database
# Implement membership card
# Implement admin and staff things








# TASK TWO:
# Make another .py file which will have the APIs (named Controller.py)
# The first API is (getAPI) /getMenu (which will get the menu and return it)        (use what was written in display menu written)
# The second API is (post API) /createMenu (which will help insert the values into the columns for menu)
# The third API is (update API) /updateValue (which will update the value in the menu using the input in the URL)
# EX for third API: menu/itemId/*name=*something* or price=*something*

# TASK THREE:
# Figure out how to take the input in Jenkins (which will then return a generated bill in the console)

# Connect Python to Jenkins??


# TASK FOUR:
# Membership card (has extra benefits: Extra 10% off bonus discount, but card is limited only to 10 visits)
# If membership card use has already had 10 visits, ask whether customer would like to renew
# Figure out how to make the membership card and keep track of it

# 1. Add column in customer database named membership card (where the value can be either True or False
# based on whether the customer has the card or not)
# 2. Add another column in customer database named membership visits (where the value can be from 0 to 10
# based on how many visits the customer has with their membership card)
# 3. When a membership reaches 10 visits, ask the customer whether they would like to renew their membership card
# and reset their visit count if they renew.

# If the customer renews, set membership visits to 0 and keep membership card as True
# If the customer doesn't renew, set membership card to False and reset membership visits to 0
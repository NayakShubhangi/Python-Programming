import streamlit as st
import pandas as pd
from DigitalClock import clockDigital
from Model import session, menu, customers, membership_card, admin, discounts
import random
from Login import authentication
import sys
from Application import databaseInfoCollection


# total = 0

# def receiptGeneration(total, membershipDiscount, role_discount, guessDiscount, payment_method):
#     st.subheader("Receipt")
#     st.write(f"Subtotal (Before Discount): ${total}")
#     if membershipDiscount:
#         st.write(f"Membership Card Discount: {membershipDiscount}%")
#     if role_discount:
#         st.write(f"Role Discount: {role_discount}%")
#     if guessDiscount:
#         st.write(f"Membership Card Discount: {guessDiscount}%")
#     if total_discount:
#         st.write(f"You saved ${total_discount} after all discounts")
#     st.write(f"Grand Total: ${final_amount}")
#     st.write(f"Payment Mode: {payment_method}")

def main_menu():
    db = session
    menu_items, roles = databaseInfoCollection()
    
    st.title("Welcome to Restaurant")
    st.image("C:\\Users\\amrit\\Desktop\\PythonProgramming\\PythonProjects\\RestaurantManagementSystem\\img3.jpg", caption="Enjoy Your Meal", use_container_width=True)

    name = st.text_input("Enter Your Name: ")
    mobile_number = st.text_input("Enter Your Mobile Number: ")
    st.header("Menu")
    selected_items = {}
    for item, price in menu_items.items():
        if st.checkbox(f"{item}-${price}"):
            quantity = st.number_input(f"Enter the Quantity for the {item}: ", min_value=1, step=1, key=item)
            selected_items[item] = {
                "Price": price,
                "Quantity": quantity
            }

    st.header("Special Membership Discounts")
    hasMemCard = st.radio("Do You Have a Membership Card?", ("Yes", "No"))
    membershipDiscount = 10 if hasMemCard == "Yes" else 0

    selected_roles = st.multiselect("Select All Applicable Roles For Discount: ", options=list(roles.keys()))
    role_discount = sum([roles[role] for role in selected_roles])

    st.subheader("Guess a Random Number and Win a 10% Discount!")
    guessDiscount = 0
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False

    randomnum = random.randrange(0, 10)
    st.session_state.randomnum = randomnum
    guess = st.number_input("Enter a number between 0 and 9: ", min_value=1, step=1)

    if st.button("See If You Guessed It", disabled=st.session_state.button_clicked):
        st.session_state.button_clicked = True
        if guess == randomnum:
            guessDiscount = 10
            st.write(f"Congratulations! You have guessed the number, which was {randomnum}. You Have Won the 10% Discount!")
        else:
            st.write(f"You Were Unable to Guess the Secret Number. It Was {randomnum}.")
        st.write("Thanks For Playing!")

    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Generate Bill"):
            bill_data = []
            total, total_discount, final_amount = 0, 0, 0
            for item, details in selected_items.items():
                item_total = details['Price']*details['Quantity']
                bill_data.append([item, details["Quantity"], details["Price"], item_total])
                total += item_total
            if guessDiscount:
                total_discount = total*((membershipDiscount/100)+(role_discount/100)+(guessDiscount/100))
            else:
                total_discount = total*((membershipDiscount/100)+(role_discount/100))
            final_amount = total-total_discount
            data_frame = pd.DataFrame(bill_data, columns=["Item", "Quantity", "Price Per Item", "Total Price"])
            st.subheader("Bill Summary")
            st.dataframe(data_frame)
            st.write(f"Subtotal: {total}")
            st.write(f"Discount Applied: {total_discount}")
            st.write(f"Grand Total: {final_amount}")

    st.subheader("Select a Payment Mode")
    col1, col2, col3 = st.columns(3)
    # Fix code so that the function works (scope issue for some reason...)
    with col1:
        if st.button('Credit Card'):
            payment_method = "Credit Card"
            # nonlocal total
            st.subheader("Receipt")
            st.write(f"Subtotal (Before Discount): ${total}")
            if membershipDiscount:
                st.write(f"Membership Card Discount: {membershipDiscount}%")
            if role_discount:
                st.write(f"Role Discount: {role_discount}%")
            if guessDiscount:
                st.write(f"Membership Card Discount: {guessDiscount}%")
            if total_discount:
                st.write(f"You saved ${total_discount} after all discounts")
            st.write(f"Grand Total: ${final_amount}")
            st.write(f"Payment Mode: {payment_method}")
            # receiptGeneration(total, membershipDiscount, role_discount, guessDiscount, payment_method)
    with col2:
        if st.button('Debit Card'):
            payment_method = "Debit Card"
            receiptGeneration(total, membershipDiscount, role_discount, guessDiscount, payment_method)
    with col3:
        if st.button('Cash'):
            payment_method = "Cash"
            receiptGeneration(total, membershipDiscount, role_discount, guessDiscount, payment_method)


    # Shifted TASK TWO: (DONE)
    # Make receipt automatic in UI after payment mode is selected
    # (subtotal, detailed discount total with all discounts applied, grand total, and payment mode)


if __name__ == '__main__':
    if authentication():
        main_menu()


# TASK ONE (PARTIAL?/DONE):
# Integrate this with the actual code
# 1. Take input for customer details (done)
# 2. Get all the details like menu and things like that (and role too) (done)
# 3. Payment method validation thing (done)

# Add two more role discount records to the discounts table


# TASK ONE: (DONE)
# Update the code so that all things related to the database (like menu and roles) come from Application.py

# TASK ONE:
# Make reciept automatic in UI after payment mode is selected
# (subtotal, detailed discount total with all discounts applied, grand total, and payment mode)
# Error for some reason, saying that the variables don't exist apparently, though they clearly do
# (maybe they're in a different scope)
# ARE IN DIFFERENT SCOPES (Use global/nonlocal maybe??)

# TASK TWO: (DONE)
# Find all of the inbuilt methods/functions which will help to remove/delete an element in all iterables
# EX: List -> Find the inbuilt methods/functions which will help remove/delete an element

# List: .remove(), .pop(), del, .clear()
# Dictionary: .pop(), .popitem(), del, .clear()
# Set: .remove(), .discard(), .pop(), .clear()
# Tuples (Immutable)
# Strings (Immutable)

# TASK THREE: (DONE)
# Go through and get a brief understanding of: Ollama model, Rag, Agentic AI (Give an example for each if possible)

# Ollama model: A simple tool that allows users to run Large Lanuage Models (LLMs) directly on their own computers.

# RAG: Stands for Retrieval-Augmented Generation and is a technique in AI that enhances the accuracy and relevance of LLMs
# by incorporating external knowledge sources during the generation process, rather than relying on just internal training data.
# It would be good to use when you need real-time access to the latest data, particularly when accuracy is important.

# Agentic AI: Artificial intelligence systems designed to operate in such a way that they can make decisions
# and take actions independently to achieve specific goals with little to none human assistance.
# It would be good to use when complex, multi-step tasks are involved, in which case it would break those tasks down into sub-tasks.




# TASK TWO: (DONE, I THINK)
# Brush up on github
# figure out how to upload directly from vscode to github




# TASK THREE: (DONE)
# Change the login function so that it only works for credentials with admin

# TASK THREE/FOUR: (DONE)
# insert id from admins to credentials (foreign key reference from admin table to credentials)
# add a username and password for both
# drop table, then remake credentials with no name, since name isn't being used here (and change id to a foreign key somehow)






# TASK TWO (PROBLEM):
# Add a background image/color thing for the UI (st.*something for background*) and try it
# Issue: Everything I found talks about CSS with streamlit but not about anything just in streamlit

# TASK THREE (DONE):
# Brush up on password input (with the special hiding thing) in getpass
# just import getpass, then use getpass.getpass()


# TASK FOUR (PROBLEM):
# Set a very small digital clock in the right corner that's running all the time
# use help from the digitalClock.py as reference
# Issue: Clock doesn't show up and will conflict with the other code since it runs forever


# TASK FIVE (DONE):
# Try to integrate the number guessing game that will give the customer 10% discount if they get it right on first try

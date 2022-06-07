#import Module
import streamlit as st


st.title("FREE INVOICE GENERATOR")

# st.form('my_form_identifier')
col1, col2 = st.columns(2)

with col1:
    company_name = st.text_input('Company Name:')
    Company_email = st.text_input('Company Email:')
    Company_Phone = st.text_input('Company Mobile Number:')

with col2:
    recipients_name = st.text_input('Recipients Name:')
    recipients_email = st.text_input('Recipients Email:')
    recipients_phone = st.text_input('Recipients Phone:')

# Invoice Items
icol1, icol2, icol3 = st.columns(3)

# Invoice Items
invoice_item = {}
invoice_history = []


def invoice():
    for i in range(0, 5):
        current_item = 0

    while True:
        with icol1:
            product = st.text_input('Item', key=current_item)
        current_item += 1

        with icol2:
            qty = st.number_input('Quanitity', key=current_item)

        with icol3:
            price = st.number_input('Price', key=current_item)

        invoice_item = {'Product': product, 'Quantity': qty, 'Price': price}
        invoice_history.append(invoice_item)

        if current_item == i:
            break


invoice()

grand_total = 0

if(st.button('Submit')):
    for index, item in enumerate(invoice_history):
        item_total = item['Quantity'] * item['Price']
        grand_total = grand_total + item_total
        item_total = 0

st.text("Total Amount in Naira")
st.success(grand_total)

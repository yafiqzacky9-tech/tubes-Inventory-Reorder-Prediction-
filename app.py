import streamlit as st
import joblib
import numpy as np

model = joblib.load("model_inventory.pkl")

st.title("Inventory Reorder Prediction")

category = st.number_input("Category", value=0)
supplier = st.number_input("Supplier", value=0)
warehouse = st.number_input("Warehouse", value=0)
unit = st.number_input("Unit", value=0)

purchase_price = st.number_input("Purchase Price")
selling_price = st.number_input("Selling Price")
current_stock = st.number_input("Current Stock")
minimum_stock = st.number_input("Minimum Stock")
maximum_stock = st.number_input("Maximum Stock")

avg_daily_sales = st.number_input("Average Daily Sales")
stockout_days = st.number_input("Stockout Days")
lead_time_days = st.number_input("Lead Time Days")

transactions_30days = st.number_input("Transactions (30 Days)")
sold_30days = st.number_input("Sold (30 Days)")
stock_percentage = st.number_input("Stock Percentage")
days_of_supply = st.number_input("Days of Supply")

if st.button("Predict"):

    data = np.array([[
        category,
        supplier,
        warehouse,
        unit,
        purchase_price,
        selling_price,
        current_stock,
        minimum_stock,
        maximum_stock,
        avg_daily_sales,
        stockout_days,
        lead_time_days,
        transactions_30days,
        sold_30days,
        stock_percentage,
        days_of_supply
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Need Reorder")
    else:
        st.success("No Reorder Needed")

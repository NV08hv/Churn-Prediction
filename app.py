
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time


def load_model():
    loaded_pipeline = joblib.load('pipeline12.joblib')
    return loaded_pipeline

def predict_churn(model, input_data):
    columns = ['Unnamed: 0', 'Tenure', 'PreferredLoginDevice', 'CityTier', 'WarehouseToHome', 'PreferredPaymentMode', 'Gender', 'HourSpendOnApp',
       'PreferedOrderCat', 'SatisfactionScore', 'MaritalStatus', 'Complain',
       'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount',
       'DaySinceLastOrder', 'CashbackAmount', 'Tenure_bins',
       'avg_hour_spend_on_app_per_order', 'cashback_amount_per_month',
       'DaySinceLastOrder_2']
    input_data = pd.DataFrame([input_data], columns=columns)
    prediction = model.predict(input_data)
    return prediction[0]

model = load_model()

st.title("Churn Prediction App")
st.header("Input Customer Information")
st.snow()
feature = []
col1 = 2204
feature.append(col1)
tenure = st.number_input('Tenure (Months)', min_value=0, max_value=72)
feature.append(tenure)

PreferredLoginDevice = st.selectbox('Prefer Login Device', ['Phone', 'Computer'])
feature.append(PreferredLoginDevice)

CityTier = st.selectbox('CityTier', [1, 2, 3])
feature.append(CityTier)

WarehouseToHome = st.number_input('Distance from Warehouse to Home', min_value=0, max_value=1000)
feature.append(WarehouseToHome)

PreferredPaymentMode = st.selectbox('Preferred Payment Mode', ['Debit Card', 'Credit Card', 'E wallet', 'Cash on Delivery', 'UPI','CC'])
feature.append(PreferredPaymentMode)



gender = st.radio('Pick your Gender', ['Male', 'Female'])
feature.append(gender)

HourSpendOnApp = st.number_input('Distance from Warehouse to Home', min_value=0, max_value=10)
feature.append(HourSpendOnApp)

PreferedOrderCat = st.selectbox('Prefered Order Categories', ['Laptop & Accessory', 'Mobile', 'Fashion', 'Grocery', 'Others'])
feature.append(PreferedOrderCat)

SatisfactionScore = st.number_input('Satisfaction Score', min_value=1, max_value=5)
feature.append(SatisfactionScore)

MaritalStatus = st.selectbox('Marital Status', ['Married', 'Single', 'Divorced'])
feature.append(MaritalStatus)             

Complain = st.number_input('complain', min_value=0, max_value=1)
feature.append(Complain)

OrderAmountHikeFromlastYear = st.number_input('Order Amount Hike From last Year', min_value=0, max_value=100)
feature.append(OrderAmountHikeFromlastYear)

CouponUsed = st.number_input('Coupon Used', min_value=0, max_value=50, value=0)
feature.append(CouponUsed)

OrderCount = st.number_input('Order Count', min_value=0, max_value=100, value=1)
feature.append(OrderCount)

DaySinceLastOrder = st.number_input('Day Since Last Order', min_value=0, max_value=100, value=0)
feature.append(DaySinceLastOrder)

CashbackAmount = st.number_input('Cash back Amount', min_value=0, max_value=1000000, value=0)
feature.append(CashbackAmount)

Tenure_bins = st.selectbox('Tenure bins', ['[0, 10)', '[10, 20)', '[20, 30)', '[30, 40)', '[60, 70)'])
feature.append(Tenure_bins)

avg_hour_spend_on_app_per_order = st.number_input('average hour spend on app per order', min_value=0, max_value=10, value=0)
feature.append(avg_hour_spend_on_app_per_order)

cashback_amount_per_month = st.slider('cashback amount per month', min_value=0, max_value=1000000, value=0)
feature.append(cashback_amount_per_month)

DaySinceLastOrder_2 = DaySinceLastOrder * DaySinceLastOrder
feature.append(DaySinceLastOrder_2)


if st.button("Predict Churn"):
    prediction = predict_churn(model, feature)
    if prediction == 1:
        st.write("The customer is likely to churn.")
    else:
        st.write("The customer is not likely to churn.")
    st.success("Successfully Prediction")



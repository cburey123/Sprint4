import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("vehicles_us.csv")

# Header
st.header("Car Advertisement Dashboard 🚗")

# Histogram
st.subheader("Price Distribution")
fig1 = px.histogram(df, x="price", nbins=50, title="Distribution of Car Prices")
st.plotly_chart(fig1)

# Scatter plot with checkbox
st.subheader("Price vs Odometer")
show_color = st.checkbox("Color by Model Year")

if show_color:
    fig2 = px.scatter(df, x="odometer", y="price", color="model_year",
                      title="Price vs Odometer (Colored by Model Year)")
else:
    fig2 = px.scatter(df, x="odometer", y="price",
                      title="Price vs Odometer")
st.plotly_chart(fig2)

import streamlit as st
import pandas as pd
import psycopg2

st.title("Smart City Traffic Dashboard")

conn = psycopg2.connect(
    host='localhost',
    database='smartcity',
    user='admin',
    password = 'admin123',
    port=5432
)

query = "select * from traffic_data order by timstamp desc limit 20"
df = pd.read_sql(query, conn)

st.dataframe(df)
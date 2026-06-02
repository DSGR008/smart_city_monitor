import streamlit as st
import pandas as pd
import psycopg2
import streamlit_autorefresh as st_autorefresh

st_autorefresh.autorefresh(interval=5000)

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

if not df.empty:
    tot_veh = df['vehicle_count'].sum()
    avg_speed = round(df['avg_speed'].mean(), 2)
    latest_traffic = df.iloc[0]
else:
    tot_veh = 0
    avg_speed = 0
    latest_traffic = "N/A"

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Total Vehicles", tot_veh)
with c2:
    st.metric("Average Speed (km/h)", avg_speed)
with c3:
    st.metric("latest traffic" ,latest_traffic)

chart_data = df[['timstamp', 'vehicle_count']].set_index('timstamp')
chart_data = chart_data.sort_values("timstamp")

st.line_chart(chart_data.set_index('timstamp'))

st.dataframe(df)
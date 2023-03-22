import streamlit as sl
import pandas as pd
import requests as req
import snowflake.connector

sl.header("Zena's Amazing Athleisure Catalog")


sf_conn=snowflake.connector.connect(**sl.secrets["snowflake"])
with sf_conn.cursor() as cur:
  cur.execute("SELECT * FROM CATALOG")
catData = cur.fetchall()
sf_conn.close()

sl.dataframe(catData)

import streamlit as sl
import pandas as pd
import requests as req
import snowflake.connector as sflake

sl.header("Zena's Amazing Athleisure Catalog")


sf_conn=sflake.connect(**streamlit.secrets["snowflake"])
with sf_conn.cursor() as cur:
  cur.execute("SELECT * FROM CATALOG")
catData = cur.fetchall()
sf_conn.close()

streamlit.dataframe(catData)

import streamlit as sl
import pandas as pd
import requests as req
import snowflake.connector

sl.header("Zena's Amazing Athleisure Catalog")


sf_conn=snowflake.connector.connect(**sl.secrets["snowflake"])
with sf_conn.cursor() as cur:
  cur.execute("SELECT COLOR_OR_STYLE FROM catalog_for_website")
  styleList = cur.fetchall()
#sf_conn.close()

styleListDF=pd.DataFrame(styleList)
#styleListDF=styleListDF.set_index('COLOR_OR_STYLE')

sl.write(styleListDF)

styleSelected = sl.selectbox("Pick a sweatsuit color or style:", list(styleListDF[0]))

product_caption = 'Our warm, comfortable, ' + styleSelected + ' sweatsuit

#cur.execute("SELECT DIRECT_URL  FROM catalog_for_website WHERE COLOR_OR_STYLE = '"+ styleSelected +"';")

#selectedDF=cur.fetchone()

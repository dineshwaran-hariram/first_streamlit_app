import streamlit as sl
import pandas as pd
import requests as req
import snowflake.connector

sl.header("Zena's Amazing Athleisure Catalog")


sf_conn=snowflake.connector.connect(**sl.secrets["snowflake"])
cur=sf_conn.cursor()
cur.execute("SELECT COLOR_OR_STYLE FROM catalog_for_website")
styleList = cur.fetchall()


styleListDF=pd.DataFrame(styleList)
#styleListDF=styleListDF.set_index('COLOR_OR_STYLE')

#sl.write(styleListDF)
color_list = styleListDF[0].values.tolist()

styleSelected = sl.multiselect("Pick a sweatsuit color or style:", list(color_list))

product_caption = 'Our warm, comfortable, ' + styleSelected[0] + ' sweatsuit'

cur.execute("SELECT DIRECT_URL  FROM catalog_for_website WHERE COLOR_OR_STYLE = '"+ styleSelected +"';")

selectedDF=cur.fetchone()

sl.image(selectedDF[0],width=400,caption=product_caption)

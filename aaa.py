#  streamlit app

import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

#   to run:
# cd /d c:\aaC\vEnv\vEnvPy
# vEnv\Scripts\activate
# cd /d c:\peg\UNIS\Prg\Py\PpPy\excel-webapp-streamlit\
# streamlit run aaa.py

help_input = r'''
  to run:
cd /d c:\aaC\vEnv\vEnvPy
vEnv\Scripts\activate
cd /d C:\peg\z1drv\OneDrive\aaEgp_P2E2\1Drv\qqq_Prj\ppBB\
streamlit run aaa.py
'''

st.set_page_config(page_title='su tu Survey Results')
st.header('su tu Survey Results 2021')
st.subheader('au tu Was the tutorial helpful?')
st.subheader('pokus')
st.text('This is some text.')
st.text(help_input)

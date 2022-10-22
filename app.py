import streamlit as st
import pandas as pd
from utils import Database
db = Database()

st.title('SQLite Test')


raw_data = db.get_data()
data = db.transform(raw_data)
df = pd.DataFrame(data)
amount = st.slider("Reps", 5, 50, 10, 5)
df[df.reps > amount]
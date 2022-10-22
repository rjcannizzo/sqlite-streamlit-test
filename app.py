import streamlit as st
import pandas as pd
from utils import get_data, transform
st.title('SQLite Test')


raw_data = get_data()
data = transform(raw_data)
df = pd.DataFrame(data)
amount = st.slider("Reps", 5, 50, 10, 5)
df[df.reps > amount]
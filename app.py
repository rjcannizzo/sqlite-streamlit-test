import streamlit as st
import pandas as pd
from utils import get_data, transform
st.title('SQLite Test')


raw_data = get_data()
data = transform(raw_data)
df = pd.DataFrame(data)
df[df.reps % 2 == 0]
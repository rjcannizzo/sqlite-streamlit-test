import streamlit as st
import sqlite3

class Database:

    @st.cache(suppress_st_warning=True)
    def get_data(self):
        st.write('getting data from db...')
        conn = sqlite3.connect('exercise.db')
        cursor = conn.cursor()
        cursor.execute('select * from exercise')
        return cursor.fetchall()

    def transform(self, input):
        data = []
        for item in input:
            date, exercise, reps, _ = item
            data.append(dict(date=date, exercise=exercise, reps=reps))
        return data
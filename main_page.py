import streamlit as st
import Zagoskina
import borisov


st.title('Проект "Титаник"')

vladimir = "Борисов - вариант 6."
marina = "Загоскина - вариант 5."

members_list = [vladimir, marina]

member = st.radio("Выберите, чью задачу хотите рассмотреть", members_list)

if member == vladimir:
    borisov.var6()
elif member == marina:
    Zagoskina.var5()

import streamlit as st
import Zagoskina
import borisov
import kozlova

st.title('HomeWork 10')

vladimir = "Борисов - вариант 6."
marina = "Загоскина - вариант 5."
olga = 'Козлова - вариант 7'


members_list = [vladimir, marina, olga]

member = st.radio("Выберите, чью задачу хотите рассмотреть", members_list)

if member == vladimir:
    borisov.var6()
elif member == marina:
    Zagoskina.var5()
elif member == olga:
    kozlova.var7()

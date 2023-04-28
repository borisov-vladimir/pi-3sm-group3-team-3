import streamlit as st
import Zagoskina
import borisov
import kozlova
import ivushkin

st.title('HomeWork 10')

vladimir = "Борисов Владимир- вариант 6."
marina = "Загоскина Марина- вариант 5."
olga = 'Козлова Ольга- вариант 7'
alex = 'Ивушкин Александр- вариант 4'
natalya 'Зайцева Наталия - вариант 2'

members_list = [vladimir, marina, olga, alex]

member = st.radio("Выберите, чью задачу хотите рассмотреть", members_list)

if member == vladimir:
    borisov.var6()
elif member == marina:
    Zagoskina.var5()
elif member == olga:
    kozlova.var7()
elif member == alex:
    ivushkin.var4()
elif member == natalya:
    ivushkin.var4()
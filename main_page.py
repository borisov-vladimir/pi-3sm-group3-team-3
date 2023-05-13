import streamlit as st
import zagoskina
import borisov
import kozlova
import ivushkin
import zayceva

st.title('HomeWork 10')
st.subheader('группа 3 см, команда 3')

vladimir = "Борисов Владимир"
marina = "Загоскина Марина"
olga = 'Козлова Ольга'
alex = 'Ивушкин Александр'
natalya = 'Зайцева Наталия'

var = [vladimir, marina, olga, alex, natalya]

var = st.radio("Выберите вариант:", var)

if var == vladimir:
    borisov.var6()
elif var == marina:
    zagoskina.var5()
elif var == olga:
    kozlova.var7()
elif var == alex:
    ivushkin.var4()
elif var == natalya:
    zayceva.var2()

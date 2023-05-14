import streamlit as st
import zagoskina_change_def
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
    st.subheader('Вариант 5: вывести Pclass, Name, Age спасенных с именами начинающихся на введенный текст')
    zagoskina_change_def.variant5()
elif var == olga:
    kozlova.var7()
elif var == alex:
    ivushkin.var4()
elif var == natalya:
    zayceva.var2()

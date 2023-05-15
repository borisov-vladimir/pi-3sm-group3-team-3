import streamlit as st
import pandas as pd
import zagoskina
import borisov
import kozlova
import ivushkin
import zayceva
#import tst

#st.title('HomeWork 10')
st.subheader('группа 3 см, команда 3')

vladimir = "Борисов Владимир"
marina = "Загоскина Марина"
olga = 'Козлова Ольга'
alex = 'Ивушкин Александр'
natalya = 'Зайцева Наталия'

var = [vladimir, marina, olga, alex, natalya]

var = st.radio("Выберите вариант:", var)

with open("data.csv") as file:
    data = file.readlines()
    df = pd.read_csv('data.csv', delimiter=',')

if var == vladimir:
    borisov.var6(data)
elif var == marina:
    zagoskina.var5(data)
elif var == olga:
    kozlova.var7(df)
elif var == alex:
    ivushkin.var4(df)
elif var == natalya:
    zayceva.var2()

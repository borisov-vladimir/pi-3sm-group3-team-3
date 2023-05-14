import pandas as pd
import streamlit as st
def var4(data):
    st.subheader('Вариант 4: Вывести имена пассажиров, стоимость билета которых была выше указанной')
    #data = pd.read_csv('data.csv')
    fare = st.slider('Выберите минимальное значение цены билета:', min_value=0, max_value=200)
    passengers = data.loc[data['Fare'] > fare, ['Name', 'Fare']]
    st.write(passengers)

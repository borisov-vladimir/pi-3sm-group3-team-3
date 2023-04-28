#Козлова О.С. 3см 7 вариант
import streamlit as st
import pandas as pd

def var7():
    st.header('Вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен/нет')

    df = pd.read_csv('data.csv', delimiter=',')
    df_nullcost = df[(df['Fare'] == 0)]

    choice = st.radio('Вас интересует список:', ['Спасен', 'Не спасен'])
    if choice == 'Спасен':
        st.dataframe(df_nullcost[(df_nullcost['Survived'] == 1)])
    else:
        st.dataframe(df_nullcost[(df_nullcost['Survived'] == 0)])
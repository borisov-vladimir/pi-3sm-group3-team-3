def var4_list(df, fare):
    result = pd.DataFrame(columns=['Name', 'Fare'])
    result = df.loc[df['Fare'] > fare, ['Name', 'Fare']]
    return result

def var4(df):
    st.subheader('Вариант 4: Вывести имена пассажиров, стоимость билета которых была выше указанной')
    fare = st.slider('Выберите минимальное значение цены билета:', min_value=0, max_value=270)
    st.write(var4_list(df, fare))
import pandas as pd
import streamlit as st

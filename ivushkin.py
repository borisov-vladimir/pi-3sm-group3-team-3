import streamlit as st
def var6_list(df, fare):
    result = df.loc[df['Fare'] > fare, ['Name', 'Fare']]
    return result

def var4(df):
    st.subheader('Вариант 4: Вывести имена пассажиров, стоимость билета которых была выше указанной')
    fare = st.slider('Выберите минимальное значение цены билета:', min_value=0, max_value=500)
    st.write(var6_list(df, fare))

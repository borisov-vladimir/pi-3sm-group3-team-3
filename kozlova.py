import streamlit as st
def var7_list(df, Survived):
    df_nullcost = df[(df['Fare'] == '0')]
    if Survived == 'Спасен':
        result = df_nullcost[(df_nullcost['Survived'] == 1)]
    else:
        result = df_nullcost[(df_nullcost['Survived'] == 0)]
    return result
def var7(df):
    st.subheader('Вариант 7: вывести данные пассажиров с билетом нулевой стоимости, выбрав спасен / нет')
    Survived = st.radio('Вас интересует список:', ['Спасен', 'Не спасен'])
    st.dataframe(var7_list(df, Survived))

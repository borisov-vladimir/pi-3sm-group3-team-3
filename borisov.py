import streamlit as st
def var6_list(data, pclass, sex):
    result = []
    for line in data:
        lst = line.rstrip().split(',')
        if lst[1] == "1" and lst[2] == pclass and lst[5] == sex:
            name = lst[3] + lst[4]
            result.append({"Имя": name[1:-1], "Пол": lst[5], "Возраст": lst[6]})
    return result

def var6():
    st.subheader('Вариант 6: вывести Name, Sex, Age спасенных пассажиров указанного класса и пола.')
    pclass = st.selectbox("Укажите класс билета", ['1', '2', '3'])
    sex = st.radio("Укажите пол", ['М', 'Ж'])
    if sex == 'М':
        sex = 'male'
    else:
        sex = 'female'
    with open("data.csv") as file:
        st.dataframe(var6_list(file, pclass, sex))

import streamlit as st

def var6():
    st.text('Вывести Name, Sex, Age спасенных пассажиров указанного класса и пола')
    pclass = st.selectbox("Укажите класс билета", ['1','2','3'])
    sex = st.radio("Укажите пол", ['М','Ж'])
    if sex == 'М':
        sex = 'male'
    else:
        sex = 'female'
    x = []
    with open("data.csv") as file:
        i = 0
        for line in file:
            lst = line.rstrip().split(',')
            if lst[1] == "1" and lst[2] == pclass and lst[5] == sex:
                i = i + 1
                name = lst[3] + lst[4]
                x.append({"Имя": name[1:-1], "Пол": lst[5], "Возраст": lst[6]})
    st.dataframe(x)


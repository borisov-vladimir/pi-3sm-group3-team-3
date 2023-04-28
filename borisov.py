import streamlit as st

def var6():
    st.markdown('Владимир Борисов, группа 2022-ФГиИБ-ПИ-3см')
    st.subheader('задание 9, вариант 6')
    pclass = st.selectbox("Укажите класс билета", ['1','2','3'])
    sex = st.radio("Укажите пол", ['М','Ж'])
    if sex == 'М':
        sex = 'male'
    else:
        sex = 'female'
    lst = []
    with open("data.csv") as file:
        i = 0
        for line in file:
            lst = line.rstrip().split(',')
            if lst[1] == "1" and lst[2] == pclass and lst[5] == sex:
                i = i + 1
                name = lst[3] + lst[4]
                lst.append({"Имя": name[1:-1], "Пол": lst[5], "Возраст": lst[6]})
    st.dataframe(lst)

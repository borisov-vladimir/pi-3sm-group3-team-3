import streamlit as st

def var2():
    st.subheader('Вариант 2: Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет')
    Survived = st.radio('Укажите пассажир спасен:', ['Да', 'Нет'])
    sex = st.radio("Укажите пол", ['М','Ж'])
    if sex == 'М':
        sex = 'male'
    else:
        sex = 'female'
    if Survived == 'Да':
        Survived = '1'
    else:
        Survived = '0'

    result = []
    with open("data.csv") as file:
        for line in file:
            lst = line.rstrip().split(',')
            if lst[1] == Survived and lst[5] == sex:
                name = lst[3] + lst[4]
                result.append({"Имя": name[1:-1], "Возраст": lst[6], "Класс билета": lst[2]})
    st.dataframe(result)

var2()
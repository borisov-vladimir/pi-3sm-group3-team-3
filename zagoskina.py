import streamlit as st
def var5():
    st.subheader('Вариант 7: вывести Pclass, Name, Age спасенных с именами начинающихся на введенный текст')
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    text_input = st.text_input("Введите начало имени")

    lstName = []
    lstPlclass = []
    lstAge = []
    with open('data.csv') as data_file:
        for line in data_file:
            lst = line.split(',')
            name =lst[3] + lst[4]
            if (lst[1] == '1' and name[1:-1].startswith((text_input))): # имя совпадает и он спасён
                lstAge.append(lst[6])
                lstPlclass.append(lst[2])
                lstName.append(name[1:-1])
    passangers = {'Имя': lstName, 'Возраст': lstAge, 'Класс': lstPlclass }
    st.dataframe(passangers)
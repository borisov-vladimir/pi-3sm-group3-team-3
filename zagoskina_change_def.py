import streamlit as st
def get_result(data_file, starts_with_text):
        text_input = starts_with_text
        out_list = []
        for line in data_file:
            lst = line.split(',')
            name = lst[3] + lst[4]
            if (lst[1] == '1' and name[1:-1].startswith(text_input)): # имя совпадает и он спасён
                out_list.append(lst[6] + " " +name+ " "+ lst[2])
        return (out_list)


def variant5():
    with open('data.csv') as data_file:
        data = data_file.readlines()
    starts_with_text = st.text_input("Введите начало имени")
    st.dataframe(get_result(data, starts_with_text))

variant5()
from zayceva import get_pass_list


def test_var2_def_1():
    data = ['11,1,3,"Marguerite, Rut",female,4',
            '12,0,1,"Bonnell, Elizabeth",female,58',
            '13,1,3,"William, Henry",male,20',
            '14,1,3,"Anders, Johan",male,39']
    result = [{'Имя': 'Marguerite Rut', 'Возраст': '4', 'Класс билета': '3'}]
    assert get_pass_list(data, '1', 'female') == result


def test_var2_def_2():
    data = ['11,1,3,"Marguerite, Rut",female,4',
            '12,0,1,"Bonnell, Elizabeth",female,58',
            '13,1,3,"William, Henry",male,20',
            '14,1,3,"Anders, Johan",male,39']
    assert get_pass_list(data, '0', 'male') == []


def test_var2_def_3():
    data = ['11,1,3,"Marguerite, Rut",female,4',
            '12,0,1,"Bonnell, Elizabeth",female,58',
            '13,1,3,"William, Henry",male,20',
            '14,1,3,"Anders, Johan",male,39']
    result = [{'Имя': 'William Henry', 'Возраст': '20', 'Класс билета': '3'},
              {'Имя': 'Anders Johan', 'Возраст': '39', 'Класс билета': '3'}]
    assert get_pass_list(data, '1', 'male') == result

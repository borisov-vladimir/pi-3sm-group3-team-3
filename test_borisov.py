from borisov import var6_list


def test_var6_def_1():
    data = ['1,1,1,"Carrau, Mr. Francisco M",male,28',
            '2,1,2,"Иванов, Иван",male,33',
            '3,1,1,"Ilett, Miss. Bertha",female,17',
            '4,1,1,"Петров, Петр",male,44']
    assert var6_list(data, '1', 'male') == [{'Имя': 'Carrau Mr. Francisco M',
                                             'Пол': 'male', 'Возраст': '28'},
                                            {'Имя': 'Петров Петр',
                                             'Пол': 'male', 'Возраст': '44'}]


def test_var6_def_2():
    data = ['1,1,1,"Carrau, Mr. Francisco M",male,28',
            '2,1,2,"Иванов, Иван",male,33',
            '3,1,1,"Ilett, Miss. Bertha",female,17',
            '4,1,1,"Петров, Петр",male,44']
    assert var6_list(data, '3', 'male') == []


def test_var6_def_3():
    data = ['1,1,1,"Carrau, Mr. Francisco M",male,28',
            '2,1,2,"Иванов, Иван",male,33',
            '3,1,1,"Ilett, Miss. Bertha",female,17',
            '4,1,1,"Петров, Петр",male,44']
    assert var6_list(data, '1', 'female') == [{'Имя': 'Ilett Miss. Bertha',
                                               'Пол': 'female',
                                               'Возраст': '17'}]

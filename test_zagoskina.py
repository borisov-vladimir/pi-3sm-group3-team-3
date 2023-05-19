from zagoskina import get_result


def test_var5_def_1():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"',
            '7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S']
    assert get_result(data, 'B') == [{'Возраст': '22',
                                      'Имя': '"Braund Mr. Owen Harris"',
                                      'Класс': '3'}]


def test_var5_def_2():
    data= ['26,1,3,"Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)",female,38,1,5,347077,31.3875,,S']
    assert get_result(data, 'Asplund') == [{'Возраст': '38',
                                            'Имя': '"Asplund Mrs. Carl Oscar (Selma Augusta Emilia Johansson)"',
                                            'Класс': '3'}]


def test_var5_def_3():
    data = ['26,0,3,"Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)",female,38,1,5,347077,31.3875,,S']
    assert get_result(data, 'Asplund') == []


def test_var5_def_4():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"',
            '7,1,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S']
    assert get_result(data, 'B') == [{'Возраст': '22',
                                      'Имя': '"Braund Mr. Owen Harris"',
                                      'Класс': '3'}]


def test_var5_def_5():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"',
            '7,1,1,"BcCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S']
    assert get_result(data, 'B') == [{'Возраст': '22',
                                      'Имя': '"Braund Mr. Owen Harris"',
                                      'Класс': '3'},
                                     {'Возраст': '54',
                                      'Имя': '"BcCarthy Mr. Timothy J"',
                                      'Класс': '1'}]


def test_var5_def_6():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"',
            '7,0,1,"Braund, Mr. Owen Harris",male,54,0,0,17463,51.8625,E46,S']
    assert get_result(data, 'B') == [{'Возраст': '22',
                                      'Имя': '"Braund Mr. Owen Harris"',
                                      'Класс': '3'}]

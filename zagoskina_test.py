from zagoskina_change_def.py import get_result

def test_get_list_passangers_where_name_starts_with_text_survived_is_false_and_true():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"', '7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S' ]
    assert get_result(data, 'B') == ['22 "Braund Mr. Owen Harris" 3']

def test_get_list_passangers_where_name_starts_with_text():
    data= ['26,1,3,"Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)",female,38,1,5,347077,31.3875,,S']
    assert get_result(data, 'Asplund') == ['38 "Asplund Mrs. Carl Oscar (Selma Augusta Emilia Johansson)" 3']

def test_get_list_passangers_where_name_starts_with_text_where_survived_is_false():
    data = ['26,0,3,"Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)",female,38,1,5,347077,31.3875,,S']
    assert get_result(data, 'Asplund') == []

def test_get_list_passangers_where_name_starts_with_text_where_all_survived():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"', '7,1,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S' ]
    assert get_result(data, 'B') == ['22 "Braund Mr. Owen Harris" 3']

def test_get_list_passangers_where_all_name_starts_with_text_where_all_survived():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"', '7,1,1,"BcCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S' ]
    assert get_result(data, 'B') == ['22 "Braund Mr. Owen Harris" 3', '54 "BcCarthy Mr. Timothy J" 1']

def test_get_list_passangers_where_indentical_name_starts_with_text_survived_is_false_and_true():
    data = ['"1,1,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S"', '7,0,1,"Braund, Mr. Owen Harris",male,54,0,0,17463,51.8625,E46,S' ]
    assert get_result(data, 'B') == ['22 "Braund Mr. Owen Harris" 3']
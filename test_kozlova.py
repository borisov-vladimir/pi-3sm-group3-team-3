from kozlova import var7_list
import pandas as pd


def test_var7_def_1():
    col = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
           'Age', 'SibSp', 'Parch', 'Ticket', 'Fare']
    data = [[1, 1, 3, '"Owen Harris"', 'male', 22, 1, 0, '1', 0],
            [2, 0, 1, '"John Bradley"', 'female', 38, 1, 0, 'PC 17599', 71],
            [3, 1, 3, '"Laina"', 'female', 26, 0, 0, 'A282', 0],
            [4, 0, 1, '"Jacques Heath"', 'female', 35, 1, 0, '113803', 0]]
    df = pd.DataFrame(data, columns=col)
    val = pd.DataFrame([[1, 1, 3, '"Owen Harris"', 'male', 22, 1, 0, '1', 0],
                        [3, 1, 3, '"Laina"', 'female', 26, 0, 0, 'A282', 0]],
                       columns=col)
    assert val.equals(var7_list(df, 1).reset_index(drop=True))


def test_var7_def_2():
    col = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
           'Age', 'SibSp', 'Parch', 'Ticket', 'Fare']
    data = [[1, 1, 3, '"Owen Harris"',  'male', 22, 1, 0, '1', 0],
            [2, 0, 1, '"John Bradley"',  'female', 38, 1, 0, 'PC 17599', 71],
            [3, 1, 3, '"Laina"', 'female', 26, 0, 0, '3101282', 0],
            [4, 0, 1, '"Jacques Heath"', 'female', 35, 1, 0, '113803', 0]]
    df = pd.DataFrame(data, columns=col)
    val = df.iloc[[3]]
    assert val.equals(var7_list(df, 0))


def test_var7_def_3():
    col = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
           'Age', 'SibSp', 'Parch', 'Ticket', 'Fare']
    data = [[1, 1, 3, '"Owen Harris"', 'male', 22, 1, 0, '1', 0],
            [2, 0, 1, '"John Bradley"', 'female', 38, 1, 0, 'PC 17599', 71],
            [3, 1, 3, '"Laina"', 'female', 26, 0, 0, '3101282', 0]]
    df = pd.DataFrame(data, columns=col)
    x = var7_list(df, 0)
    x = x.to_dict()
    val = {'PassengerId': {}, 'Survived': {}, 'Pclass': {},
           'Name': {}, 'Sex': {}, 'Age': {}, 'SibSp': {},
           'Parch': {}, 'Ticket': {}, 'Fare': {}}
    assert x == val

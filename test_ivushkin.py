from ivushkin import var4_list
import pandas as pd
def test_var4_def_1():
    df = pd.DataFrame(
        [[1, 1, 3, '"Braund, Mr. Owen Harris"', 'male', 22, 1, 0, 'A / 5 21171', 0],
        [2, 0, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', 'female', 38, 1, 0, 'PC 17599', 200],
        [3, 1, 3, '"Heikkinen, Miss. Laina"', 'female', 26, 0, 0, 'STON / O2. 3101282', 400],
        [4, 0, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', 'female', 35, 1, 0, '113803', 600]],
        columns=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare'])
    result = var4_list(df, 400).reset_index(drop=True)
    val = pd.DataFrame([['"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', 600]], columns=['Name', 'Fare'])
    assert val.equals(result)

def test_var4_def_2():
    df = pd.DataFrame(
        [[1, 1, 3, '"Braund, Mr. Owen Harris"', 'male', 22, 1, 0, 'A / 5 21171', 0],
        [2, 0, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', 'female', 38, 1, 0, 'PC 17599', 200],
        [3, 1, 3, '"Heikkinen, Miss. Laina"', 'female', 26, 0, 0, 'STON / O2. 3101282', 400],
        [4, 0, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', 'female', 35, 1, 0, '113803', 600]],
        columns=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare'])
    result = var4_list(df, 300)
    val = df.loc[[2,3],['Name','Fare']]
    assert val.equals(result)

def test_var4_def_3():
    df = pd.DataFrame(
        [[1, 1, 3, '"Braund, Mr. Owen Harris"', 'male', 22, 1, 0, 'A / 5 21171', 0],
        [2, 0, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', 'female', 38, 1, 0, 'PC 17599', 200],
        [3, 1, 3, '"Heikkinen, Miss. Laina"', 'female', 26, 0, 0, 'STON / O2. 3101282', 400],
        [4, 0, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', 'female', 35, 1, 0, '113803', 600]],
        columns=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare'])
    result = var4_list(df, 700).to_dict()
    val = {'Name': {}, 'Fare': {}}
    assert result == val

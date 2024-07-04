import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

# #Тесты для проверки функции "Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст":
@pytest.mark.parametrize("input_string, expected_output",
                         [("skypro", "Skypro"),
                          ("hello world", "Hello world"),
                          ("123abc", "123abc"),
                          (" ", " "),
                          ("", "")])
def test_capitilize(utils, input_string, expected_output):
     assert utils.capitilize(input_string) == expected_output

# #Тесты для проверки функции "Принимает на вход текст и удаляет пробелы в начале, если они есть":
@pytest.mark.parametrize("input_string, expected_output",
                         [("   skypro", "skypro"),
                          ("hello world", "hello world"),
                          (" ", ""),
                          ("", "")])
def test_trim(utils, input_string, expected_output):
     assert utils.trim(input_string) == expected_output

#Тесты для проверки функции "Принимает на вход текст с разделителем и возвращает список строк":
@pytest.mark.parametrize("input_string, delimiter, expected_output",
                         [("a,b,c,d", ",", ["a", "b", "c", "d"]),
                          ("1:2:3", ":", ["1", "2", "3"]),
                          ("", ",", []),
                          ("", ' ', []),
                          ("z x c", ' ', ['z', 'x', 'c']),
                          ("x;y;z", ";", ["x", "y", "z"])])
def test_to_list(utils, input_string, delimiter, expected_output):
     assert utils.to_list(input_string, delimiter) == expected_output

#Тесты для проверки "Возвращает `True`, если строка содержит искомый символ и `False` - если нет":
@pytest.mark.parametrize("input_string, symbol, expected_output",
                         [("SkyPro", "S", True),
                          ("SkyPro", "U", False),
                          ("", "", True),
                          ("123", "1", True),
                          ("A!bc", "!", True),
                          (" ", " ", True),
                          ("ABC", "a", False), 
                          ("1 2 3", "5", False),])
def test_contains(utils, input_string, symbol, expected_output):
     assert utils.contains(input_string, symbol) == expected_output
    
#Тесты для проверки "Удаляет все подстроки из переданной строки":
@pytest.mark.parametrize("input_string, symbol, expected_output",
                         [("SkyPro", "k", "SyPro"),
                          ("SkyPro", "U", "SkyPro"),
                          ("", "", ""),
                          ("123", "1", "23"),
                          ("A!bc", "!", "Abc"),
                          (" ", " ", ""),
                          ("ABC", "a", "ABC"),
                          ("1 2 3", " ", "123"),])
def test_delete_symbol(utils, input_string, symbol, expected_output):
     assert utils.delete_symbol(input_string, symbol) == expected_output

#Тесты для проверки "Возвращает `True`, если строка начинается с заданного символа и `False` - если нет"
@pytest.mark.parametrize("input_string, symbol, expected_output",
                        [("SkyPro", "S", True),
                         ("SkyPro", "P", False),
                         ("", "", True),
                         ("123", "1", True),
                         ("A!bc", "!", False),
                         (" ", " ", True),
                         (" abc", " ", True),
                         ("ABC", "a", False),
                         (" abc ", " ", True),
                         ("ABC", "S", False),])
def test_starts_with(utils, input_string, symbol, expected_output):
    assert utils.starts_with(input_string, symbol) == expected_output

#Тесты для  проверки функции "Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет"
@pytest.mark.parametrize("input_string, symbol, expected_output",
                        [("SkyPro", "o", True),
                         ("SkyPro", "S", False),
                         ("", "", True),
                         ("123", "3", True),
                         ("A!bc", "!", False),
                         (" ", " ", True),
                         (" abc ", " ", True), #Строка начинается и заканчивается на пробел!
                         ("ABC", "a", False),
                         (" abc ", "с", False), 
                         ("ABC", "S", False),])
def test_end_with(utils, input_string, symbol, expected_output):
    assert utils.end_with(input_string, symbol) == expected_output

#Тесты для проверки функции "Возвращает `True`, если строка пустая и `False` - если нет"
@pytest.mark.parametrize("input_string, expected_output",
                         [("skypro", False),
                          ("!", False),
                          ("123", False),
                          (" ", True),
                          ("", True)])
def test_is_empty(utils, input_string, expected_output):
     assert utils.is_empty(input_string) == expected_output

#Тесты для проверки функции "Преобразует список элементов в строку с указанным разделителем"
@pytest.mark.parametrize("lst, joiner, expected_output",
                        [(["1", "2", "3", "4"], ",", "1,2,3,4"),
                        (["Sky", "Pro"], ":", "Sky:Pro"),
                        (["1", "2", "3"], "-", "1-2-3"),
                        (["x", "y", "z"], "", "xyz"),
                        (["1", "2", "3"], " ", "1 2 3"),
                        (["x", "y", "z"], ";", "x;y;z")])
def test_list_to_string(utils, lst, joiner, expected_output):
     assert utils.list_to_string(lst, joiner) == expected_output

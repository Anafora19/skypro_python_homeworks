import pytest
from Employee import Employer
from DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql+psycopg2://x_clients_db_3fmx_user:mzotw2vp4ox4nqh0xkn3kumdyaye31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

#Получаю список сотрудников из АПИ и БД, сравниваю их
def test_get_list_of_employers():
    #БД: создаю компанию
    db.create_company('Yulia testers', 'new_company')
    #БД: получаю id созданной компании
    max_id = db.last_company_id()
    print(max_id)
    #БД: создаю в этой компании нового сотрудника
    db.create_employer(max_id, "Yulia", "Serova", 800900)
    #БД: Получаю список сотрудников из созданной компании
    db_employer_list = db.get_list_employer(max_id)
    #API: получаю список сотрудников из последней созданной компании
    api_employer_list = api.get_list(max_id)
    #Сравниваю списки
    assert len(db_employer_list)==len(api_employer_list)
    #Удаляю сотрудников 
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    #БД: удалаю компанию
    db.delete(max_id)

#Добавляю сотрудника в БД и сравниваю с АПИ имя , статус и фамилию
def test_add_new_employer():
    db.create_company('Yulia testers', 'new_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Yulia", "Serova", 800900)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    #Сравниваю ID компаний
    assert response['companyId'] == max_id
    #Сравниваю имя
    assert response['firstName'] == 'Yulia'
    #Сравниваю статус
    assert response['isActive'] == True
    #Сравниваю фамилию
    assert response['lastName'] == 'Serova'
    #Удаляю сотрудника
    db.delete_employer(employer_id)
    #БД: удалаю компанию
    db.delete(max_id)

#Сравниваю информацию о сотруднике (полученная с АПИ и указанная при создании сотрудника в БД)
def test_assertion_data():
    db.create_company('Yulia testers', 'new_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Yulia", "Serova", 800900)
    employer_id = db.get_employer_id(max_id)
    #Получаю информацию о сотруднике с АПИ
    get_api_info = (api.get_info(employer_id)).json()
    #Сравниваю информацию о сотруднике
    assert get_api_info["firstName"] == "Yulia"
    assert get_api_info["lastName"] == "Serova"
    assert get_api_info["phone"] == "800900"
    #Удаляю сотрудников 
    db.delete_employer(employer_id)
    #БД: удалаю компанию
    db.delete(max_id)





    





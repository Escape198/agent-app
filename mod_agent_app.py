'''
В этом файле описаны все методы из ТЗ.

Словарь описывает ожидаемые действия:
    0 - URL,
    1 - Метод
    2 - Наш body запроса
    3 - Ожидаемый response ! Оставил пустым


Если мы хотим протестировать любой другой метод,
то в файле agent_app.py меняем первую (после import) строку на название метода
из данного файла.

Это делается вот таким быстрым действием: https://skr.sh/vDmLYdry5M3

'''


import requests


url = 'https://partner.agentapp.ru'

# auth
auth_token = ['/v1/users/obtain-token', 'post',
              {'username': 'qa@qa.qa', 'password': '111'}, {}]

requests_auth = requests.post(url + auth_token[0], data=auth_token[2])

token = requests_auth.json()['token']
headers = {'Authorization': 'Token {}'.format(token),
           'Content-Type': 'application/json'
           }

# driver
create_driver = ['/v1/insured_objects/drivers', 'post',
                 {
                     "first_name": "Имя",
                     "last_name": "Фамилия",
                     "patronymic": "Отчество",
                     "birth_date": "1990-01-01",
                     "driving_experience_started": "2010-10-10",
                     "driver_licenses": [{"credential_type": "DRIVER_LICENSE", "number": "012345",
                                          "series": "1234", "issue_date": "2010-10-10"}]},
                 {}]

# owner
create_owner = ['/v1/insured_objects/owners/natural_persons', 'post',
                {
                    "last_name": "Фамилия",
                    "first_name": "Имя",
                    "patronymic": "Отчество",
                    "birth_date": "1990-01-01",
                    "credential": [
                        {
                            "credential_type": "RUSSIAN_INTERNAL_PASSPORT",
                            "issue_date": "2017-03-08",
                            "issue_point": "УФМС",
                            "issue_point_code": "123-456",
                            "number": "123456",
                            "series": "1234"
                        }],
                    "address": [
                        {
                            "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
                            "address_type": "LEGAL_ADDRESS",
                            "region_kladr_id": "7800000000000",
                            "city_kladr_id": "7800000600000"
                        },
                        {
                            "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
                            "address_type": "ACTUAL_ADDRESS",
                            "region_kladr_id": "7800000000000",
                            "city_kladr_id": "7800000600000"
                        }
                    ]},
                {}]


# insurant
create_insurants = ['/v1/insured_objects/insurants/natural_persons', 'post',
                    {
                        "last_name": "Фамилия",
                        "first_name": "Имя",
                        "patronymic": "Отчество",
                        "birth_date": "1990-01-01",
                        "credential": [
                            {
                                "credential_type": "RUSSIAN_INTERNAL_PASSPORT",
                                "issue_date": "2017-03-08",
                                "issue_point": "УФМС",
                                "issue_point_code": "123-456",
                                "number": "123456",
                                "series": "1234"
                            }],
                        "address": [
                            {
                                "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
                                "address_type": "LEGAL_ADDRESS",
                                "region_kladr_id": "7800000000000",
                                "city_kladr_id": "7800000600000"
                            },
                            {
                                "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
                                "address_type": "ACTUAL_ADDRESS",
                                "region_kladr_id": "7800000000000",
                                "city_kladr_id": "7800000600000"
                            }
                        ]},
                    {}]


# car
create_car = ['/v3/insured_objects/cars', 'post', {
    "car_model_id": 864026180,
    "engine_power": 211,
    "vin_number": "WAUZZZ8T4BA037241",
    "number_plate": "Р904МХ178",
    "manufacturing_year": 2010,
    "credential": [
        {
            "credential_type": "VEHICLE_REGISTRATION",
            "issue_date": "2010-11-01",
            "number": "267461",
            "series": "78УН"
        }
    ]

}, {}]


# insurance_object

create_insurance_object = ['/v3/insured_objects/cars', 'post',
                           {
                               "drivers": ['fa04ef2c-5fc9-4996-a4ce-ee684b2deea7', '9546520b-c8c6-4b2a-a3f4-df4760b42eae'],
                               "owner": 'f0417f75-e37b-485d-a6ec-965c5a2a1277',
                               "car": 'b58df614-cd39-4568-b7f6-2c3c07ebe419',
                               "insurant": 'fc3263ec-75ca-45f7-9fa0-99de084b1296',
                               'manufacturing_year': 2010,
                               'car_model_id': 864026180
                           }, {}]

# 'car_mark': 'Audi', 'car_mark_id': '471', 'car_type': 'B', 'car_model': 'A5', 'car_model_id': '864026180'
# object 0397663f-bb6b-4e32-8fc9-0b165546714a

# agreements
create_agreement = ['/v3/agreements/calculations', 'post',
                    {
                        'valid_from': '2019-06-30',
                        'valid_to': '2020-06-29',
                        'insurance_period': 11,
                        'target_of_using': 'test',
                        'drivers_ids': ['fa04ef2c-5fc9-4996-a4ce-ee684b2deea7', '9546520b-c8c6-4b2a-a3f4-df4760b42eae'],
                        'is_car_without_registration': 'True',
                        'engine_power': 211,
                        'has_car_trailer': 'True',
                        'car_type': 'B',
                        'owner_registration ':'г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1',
                        'periods': []
                    }]



import json


def get_datas() -> dict:
    try:
        with open('rent_a_car/DB.json') as f:
            datas = json.load(f)
    except:
        datas = {}

    return datas


def add_data(data: dict=None) -> None:
    datas = get_datas()

    id = data.pop('id')
    datas[id] = data

    with open('rent_a_car/DB.json', 'w') as f:
        json.dump(datas, f, indent=4)

import json


def get_logs() -> list:
    try:
        with open('generate_password/logs.json') as f:
            datas = json.load(f)
    except:
        datas = []

    return datas


def add_logs(datetime, pswd) -> None:
    datas = get_logs()
    new_data = {'datetime': str(datetime), 'password': pswd}

    datas.append(new_data)

    with open('generate_password/logs.json', 'w') as f:
        json.dump(datas, f, indent=4)

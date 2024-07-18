from db import (
    get_datas,
    add_data
)


#== UTILS ==#

def generate_id(datas) -> str:
    datas_list = list(datas)

    try:
        id = str(int(datas_list[-1]) + 1)
    except:
        id = 1

    return id

#== UTILS ==#


def add_car(
    *,
    marka,
    model,
    date_of_production,
    march,
    engine_volume,
    price,
    color,
    plate,
    owner_fullname,
    fin
) -> dict:
    datas = get_datas()
    id = generate_id(datas)

    data = {
        'id': id,
        'marka': marka,
        'model': model,
        'date_of_production': date_of_production,
        'march': march,
        'engine_volume': engine_volume,
        'price': price,
        'color': color,
        'plate': plate,
        'owner_fullname': owner_fullname,
        'fin': fin
    }

    add_data(data=data)

    return data

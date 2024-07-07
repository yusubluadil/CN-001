from datetime import datetime

from db import DB


today = datetime.today()


def detail_user(id: int=0) -> dict:
    if id in DB.keys():
        data = DB[id]
        data['days'] = (today - data['created_at']).days
        return data
    else:
        print('ID duzgun deyil!')
        return {}

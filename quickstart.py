""" Quickstart script for InstaPy usage """

import calendar

# imports
from siso_reservation.main import Siso
from siso_reservation.util import parse_cli_args

siso_config = {
    'login_id': 'brother79',
    'login_psw': 'rhksgud!12',
    'year': 2025,
    'month': calendar.APRIL,
    'weekdays': [{'weekday':calendar.SUNDAY, 'time': "16:00"}, ],
    # 'dates': [ { 'day': 1, 'time': "16:00" },],
    'book_info': {
        "email1": "brother79a",
        "email2": "nate.com",
        "userCnt": 14,
        "purpose": "테스트",
        "addr": "경기도 시흥시 목감남서35",
    }
}

if __name__ == "__main__":
    siso = Siso(siso_config)    
    siso.run(siso_config.get('login_id'), siso_config.get('login_psw'))
    print("done")
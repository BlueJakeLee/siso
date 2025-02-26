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
    'weekday': calendar.SUNDAY,
    'time': "16:00",
}

if __name__ == "__main__":
    siso = Siso(siso_config.get('year'), siso_config.get('month'), siso_config.get('weekday'), siso_config.get('time'))
    siso.run(siso_config.get('login_id'), siso_config.get('login_psw'))
    print("done")
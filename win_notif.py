import threading
from os.path import join, dirname, realpath

from plyer import notification

kwargs = {'title': 'Eyes exercises', 'message': "It's time for health care", 'app_name': 'Notification', 'timeout': 10,
          'app_icon': join(dirname(realpath(__file__)), 'eye3.ICO')}

notification.notify(**kwargs)

wait_time_seconds = 900
ticker = threading.Event()

while not ticker.wait(wait_time_seconds):
    notification.notify(**kwargs)

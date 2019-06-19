import threading
from plyer import notification

wait_time_seconds = 900
kwargs = {
    'title': 'Eyes exercises',
    'message': "It's time for health care",
    'app_name': 'Notification',
    'timeout': 10,
    'app_icon': r'D:\программирование\true github\notification\img\eye3.ico'
}

notification.notify(**kwargs)
ticker = threading.Event()

while not ticker.wait(wait_time_seconds):
    notification.notify(**kwargs)

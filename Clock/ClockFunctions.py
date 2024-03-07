import time


def check_update(val1, val2):
    if val1 == val2:
        return False

    return True


def set_current_time():
    current_time = time.localtime()
    return current_time.tm_sec, current_time.tm_min, current_time.tm_hour




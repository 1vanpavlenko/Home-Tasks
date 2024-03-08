from ClockArrow import ClockArrow
from ClockFace import ClockFace
from ClockFunctions import set_current_time
import turtle
import time

clock_face = ClockFace(300)
clock_arrow_sec = ClockArrow(220)
clock_arrow_min = ClockArrow(180)
clock_arrow_hour = ClockArrow(120)

clock_face.draw()
turtle.hideturtle()

min_to_update = True
hour_to_update = True

clock_arrow_sec.set_angle(6 * 0)
arrow_sec = clock_arrow_sec.draw()
clock_arrow_min.set_angle(6 * 0)
arrow_min = clock_arrow_min.draw()
clock_arrow_hour.set_angle(30 * 0)
arrow_hour = clock_arrow_hour.draw()

seconds, minutes, hours = set_current_time()
prev_sec, prev_min, prev_hours = seconds, minutes, hours

while True:
    start = time.thread_time()

    if min_to_update:
        arrow_min.clear()
        clock_arrow_min.set_angle(6 * minutes)
        arrow_min = clock_arrow_min.draw()
        min_to_update = False

    if hour_to_update:
        arrow_hour.clear()
        clock_arrow_hour.set_angle(30 * hours)
        arrow_hour = clock_arrow_hour.draw()
        hour_to_update = False

    arrow_sec.clear()
    seconds += 1
    clock_arrow_sec.set_angle(6 * seconds)
    arrow_sec = clock_arrow_sec.draw()

    end = time.thread_time()
    dur = end - start

    if dur >= 1:
        pass
    else:
        time.sleep(1 - dur)

    if seconds == 60:
        seconds = 0
        minutes += 1

    if minutes == 60:
        minutes = 0
        hours += 1

    if hours == 24:
        hours = 0

    if prev_min != minutes:
        prev_min = minutes
        min_to_update = True

    if prev_hours != hours:
        prev_hour = hours
        hour_to_update = True

'''
❓ PROMPT
You're exhausted after a long day and heading to bed, but you still have to set the alarm clock on your phone.
You already have one you set the day before, so all you have to do is update it.

To set your alarm, the hours and minutes are set independently, each by scrolling upwards or downwards.
One shift changes an hour or minute value by one, up or down.
The values are organized cyclically, which means that dragging 0 minutes downwards turns it into 59,
and dragging 59 upwards turns it into 0 (similarly, 0 hours can become 23 in one shift and vice versa).

Given the time of the previous alarm and the new desired time, what is the minimum number of scroll moves to set the new time?

Example(s)
For setTime = "07:30" and timeToSet = "08:00", the output should be
minScrollToSet(oldTime, newTime) = 31.

Shifting hours upwards once will change the alarm to "08:30", and shifting minutes 30 times downwards will change it to "08:00".
minScrollToSet("7:30", "8:00") === 31
minScrollToSet("7:00", "6:31") === 30
minScrollToSet("7:00", "6:25") === 26
'''


def min_scroll_to_set(old_time: str, new_time: str) -> int:
    # old_time: 7:30 new_time: 8:00
    mid_index = old_time.find(':')
    old_hours = int(old_time[:mid_index])  # 7
    old_minutes = int(old_time[mid_index+1:])  # 30

    new_mid_index = new_time.find(':')
    new_hours = int(new_time[:new_mid_index])  # 8
    new_minutes = int(new_time[new_mid_index+1:])  # 00

    min_hours = min(abs(old_hours-new_hours), 24-abs(old_hours-new_hours))
    min_minutes = min(abs(old_minutes-new_minutes),
                      60-abs(old_minutes-new_minutes))

    return min_hours + min_minutes


print(min_scroll_to_set("7:00", "6:25") == 26)
print(min_scroll_to_set("7:00", "6:31") == 30)
print(min_scroll_to_set("7:00", "6:25") == 26)
print(min_scroll_to_set("7:30", "8:00") == 31)
print(min_scroll_to_set("7:00", "8:00") == 1)
print(min_scroll_to_set("8:00", "8:00") == 0)
print(min_scroll_to_set("6:59", "7:01") == 3)

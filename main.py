def add_time(start, duration, start_day=None):
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_time, period = start.split()
    start_hour, start_minute = [int(x) for x in start_time.split(':')]
    dur_hour, dur_minute = [int(x) for x in duration.split(':')]

    # convert to 24h
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    total_minutes = start_hour * 60 + start_minute + dur_hour * 60 + dur_minute
    days_later = total_minutes // (24 * 60)
    minutes_today = total_minutes % (24 * 60)

    hour24 = minutes_today // 60
    minute = minutes_today % 60

    new_period = 'AM' if hour24 < 12 else 'PM'
    hour12 = hour24 % 12
    if hour12 == 0:
        hour12 = 12

    result = '{}:{:02d} {}'.format(hour12, minute, new_period)

    if start_day is not None:
        idx = DAYS.index(start_day.strip().capitalize())
        idx = (idx + days_later) % 7
        result += ', ' + DAYS[idx]

    if days_later == 1:
        result += ' (next day)'
    elif days_later > 1:
        result += ' ({} days later)'.format(days_later)

    return result

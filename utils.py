def format_duration(duration):
    hours, minutes, seconds = duration // 3600, duration // 60 % 60, duration % 60
    if hours:
        return f'{hours:d}:{minutes:02d}:{seconds:02d}'
    return f'{minutes:d}:{seconds:02d}'

def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    total_minutes = sum(listened) // 60
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {total_minutes} минут.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

"""Использование %"""

print("В команде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

"""Использование format()"""

print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {:.1f} с !".format(score_2 * team2_time / team1_num))

""" Использование f-строк"""

print(f'Команды решили: {score_1} и {score_2} задач')

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'
    output_result = f"Результат битвы: {challenge_result}"

print(f"Результат битвы: {challenge_result}")
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {round(((score_2 * team2_time / team1_num)
        + (score_1 * team1_time / team2_num)) / (score_1 + score_2), 2)} секунды на задачу!')

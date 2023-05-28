n = int(input())
res = [0]*4
for _ in range(n):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    if x > 0 and y > 0:
        res[0] = res[0]+1
    elif x < 0 and y > 0:
        res[1] = res[1]+1
    elif x < 0 and y < 0:
        res[2] = res[1]+1
    elif x > 0 and y < 0:
        res[3] = res[1]+1
print(f'Первая четверть: {res[0]}')
print(f'Вторая четверть:: {res[1]}')
print(f'Третья четверть: {res[2]}')
print(f'Четвертая четверть: {res[3]}')

a=int(input('Введите выручку '))
b=int(input('Введите издержки '))
if a>b:
    print('Прибыль')
    c=((a-b)/a)
    print ('Рентабельность выручки', c)
    e=int(input('Введите кол-во сотрудников '))
    p=(a-b)/e
    print ('Прибыль на одного сотрудника', p)
else:
    print('Убыток')
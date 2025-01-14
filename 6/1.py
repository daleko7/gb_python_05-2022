"""
1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
import time

class TrafficLight:


    def running(self):
        i = 0

        while i < 3:
            if i == 0:
                print('Красный.')
                self.__color = 'red'
                time.sleep(7)
            elif i == 1:
                print('Жёлтый.')
                self.__color = 'yellow'
                time.sleep(2)
            elif i == 2:
                print('Зелёный.')
                self.__color = 'green'
                time.sleep(7)
            i += 1


a = TrafficLight()
a.running()
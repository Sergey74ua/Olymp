'''
Гостиница для жирафов
Ограничение по времени: 1 секунда
Ограничение по памяти: 256 мегабайт
В гостинице для жирафов администрация хочет запастись подушками так, чтобы удовлетворить потребности
любого своего возможного постояльца. Известно, что жирафам в зависимости от длины их шеи нужно сложить
стопку подушек (в стопке одна или несколько подушек) толщиной от 1 до n сантиметров. При этом
администрация хочет обойтись как можно меньшим числом подушек, а среди наборов подушек, удовлетворяющих
этим требованиям, администрация выберет набор минимальной суммарной толщины, чтобы он занимал
минимальный объём в шкафу.
Помогите администрации составить нужный набор подушек, позволяющий получить стопку любой высоты
от 1 до n сантиметров включительно.

Формат входных данных
Во входных данных записано единственное целое число —  n из условия задачи (1≤n≤10^9).

Формат выходных данных
В единственной строке через пробел выведите толщину каждой подушки в этом наборе в произвольном порядке.
Если ответов несколько, выведите любой из них.

Система оценки
Решения, правильно работающие при n≤20, будут оцениваться в 20 баллов.
Решения, правильно работающие при n≤1000, будут оцениваться в 40 баллов.

Замечание
В примере из условия необходимо подобрать такой набор из минимального числа подушек, чтобы, используя
данные подушки, удавалось сложить стопку любой целочисленной толщины от 1 до 9 см. Таким набором является
набор из подушек толщиной 1,2,3,3 см. Действительно, стопку толщины 1,2,3 см можно сложить из одной подушки.
Оставшиеся числа получили так: 4=1+3, 5=2+3, 6=3+3, 7=1+3+3, 8=2+3+3, 9=1+2+3+3. Возможны и другие варианты
ответа. Выполнить условие задачи, используя только три подушки, нельзя.
'''
n = int(input())
arr = []
s = 0
while s < n:
    m = min(n - s, s + 1)
    arr.append(m)
    s += m
print(*arr)

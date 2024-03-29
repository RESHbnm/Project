print(*sorted([input() for _ in 'abc'], key=len)[::2], sep='\n')

# Кусок кода [input() for _ in 'abc'] представляет из себя так называемый list comprehension, который у нас иногда неверно называют "генератор списков", 
# но это что-то вроде того. В процессе исполнения создаётся следующий список: [input(), input(), input()]. Это выражение является сокращённой формы следующего кода:

# lst = []
# for _ in 'abc':
#     lst.append(input())

# 'abc' в данном случае пишем вместо более громоздкого range(3).

# Символ * перед списком позволяет функции print выводить не список, а его элементы через разделитель (пробел по умолчанию, но в данном случае мы используем символ 
# переноса строки вместо пробела, так что элементы списка будут выводиться построчно). Функция sorted позволяет отсортировать список, по умолчанию список сортируется 
# в алфавитном порядке, но если указать параметр key=len, как в данном случае, то сортировка происходит по длине элементов-строк. [::2] используется, чтобы сформировался 
# срез списка, в котором элементами являются только элементы исходного списка с чётными индексами (0 и 2). Таким образом в списке от исходного остаётся только первый и 
# последний элемент, а так как список отсортирован по длине, то эти первый и последний элемент будут самым коротким и самым длинным из исходного списка.

# Таким образом получается, что сначала формируется список городов при помощи выражения [input() for _ in 'abc'], потом этот список  сортируется по длине при помощи
#  функции sorted с параметром key=len: sorted([input() for _ in 'abc'], key=len). Далее выполняется срез списка для того, чтобы в нём остались первый и последний элементы
#  от исходного списка. sorted([input() for _ in 'abc'], key=len)[::2]. Затем выводим эти элементы через функцию print, используя распаковку списка (*) и разделитель \n.
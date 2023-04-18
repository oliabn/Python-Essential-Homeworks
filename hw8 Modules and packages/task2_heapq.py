import  calendar
import heapq

# heapq -  алгоритму черги купи
"""
Купи — це бінарні дерева, для яких кожен батьківський вузол має значення, 
менше або рівне будь-якому з його дочірніх вузлів. 
Ця реалізація використовує масиви, для яких 
heap[k] <= heap[2*k+1] і heap[k] <= heap[2*k+2] для всіх k, 
підраховуючи елементи з нуля.
"""

my_list = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
print(my_list)
heapq.heapify(my_list)      # Перетворення списку (my_list на купу
heapq.heappush(my_list, (6, 7))     # додати елемент в купу
print(my_list)
print(heapq.heappop(my_list))   # вернути та видалити найменший елем у купі (0)
print(my_list)
print(heapq.heappushpop(my_list, (9, 10)))   # додати елем в купу і вернути видаливши мінімальне значення з купи (1)
print(my_list)
print(heapq.heapreplace(my_list, (7, 8)))   # спочатку видаляє та повертає найменший елемент
                                            # з купи `heap`, а потім додає новий елемент `item`
                                            # Якщо купа порожня -> виняток `IndexError`
print(my_list)
iter = heapq.merge(my_list, heapq.heapify([(2, 3), (15, 16), (16, 17)]))    # Повертає iterator над
                                                                            # об'єднаними відсортованими значеннями
print(iter)
print(my_list)
print(heapq.nlargest(3, my_list))   # список з `n` найбільшими елементами з набору даних,
                                    # визначеного за допомогою ітерації `iterable`
print(heapq.nsmallest(3, my_list))  # список з `n` найменими елементами з набору даних,
                                    # визначеного за допомогою ітерації `iterable`




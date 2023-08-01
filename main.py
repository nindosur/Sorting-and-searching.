import random
        # 1
def shell_sort(list123):
    last_index = len(list123) # индекс последнего элемента
    step = len(list123)//2  # шаг сортировки
    while(step > 0):
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and list123[delta] > list123[j]:
                list123[delta], list123[j] = list123[j], list123[delta]
                j = delta
                delta = j - step
        step //= 2
    return list123


        # 2
def HeapSort(list123):
    # Формируем первоначальное дерево
    # Справа - налево перебираем элементы списка
    # Если у элемента есть потомки, делаем для каждого элемента просеку(сортировку)
    for start in range((len(list123)-2)//2, -1, -1):
        HeapSift(list123, start, len(list123)-1)
        # Первый элемент списка --> корень, является максимумом для не отсортированного списка
    for end in range(len(list123)-1, 0, -1):
        # Меняем максимум(корень) местами с элементом-потомком
        list123[end], list123[0] = list123[0], list123[end]
        HeapSift(list123, 0, end-1)

def HeapSift(list123, start, end):
    # Узел начала списка
    root = start
    # Цикл - пока есть потомки,, которые больше, чем root(родитель)
    while True:
        child = root*2+1 # левый потомок
        if child > end:
            break
        # Выбор наибольшего потомка в пределах списка
        if child + 1 <= end and list123[child] < list123[child+1]:
            child += 1
        # Если потомок больше корня, то меняем их местами при этом больший потомок  сам становится корнем
        # от которого идет дальше просека вниз по дереву
        if list123[root] < list123[child]:
            list123[root], list123[child] = list123[child], list123[root]
            root = child
        else:
            break


    # 3
def quicksort(list123, fst, lst):
    if fst >= lst:
        return
    i, j = fst, lst
    list1 = list123[fst] # случайно выбранный элемент
    while i <= j:
        while list123[i] < list1: i += 1
        while list123[j] > list1: j -= 1
        if i <= j:
            list123[i], list123[j] = list123[j], list123[i]
            i, j = i+1, j-1
    quicksort(list123, fst, j)
    quicksort(list123, i, lst)


    # 4
def oladyshki(list123):
    if len(list123) > 1:
        for i in range(len(list123), 1, -1):
            max_val = max(list123[:i])
            maxindex = list123.index(max_val)
            if maxindex + 1 != i:
                if maxindex != 0:
                    list123[:maxindex + 1] = reversed(list123[:maxindex + 1])
                list123[:i] = reversed(list123[:i])
            # print('Пример переворота: ', list123)
    return list123



list123 = [random.randint(-10,20) for i in range(50)]
print('До сортировки: ', list123)
shell_sort(list123)
print('После сортировки методом Шелла: ', list123)
HeapSort(list123)
print('Пирамидная сортировка: ', list123)
quicksort(list123, 0, len(list123)-1)
print('Быстрая сортировка: ', list123)
oladyshki(list123)
print('Оладушки: ', list123)
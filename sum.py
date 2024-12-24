def sumlist(lst):
    lst = [int(i) for i in lst]
    total = sum(lst)
    return total
x = input("Введите список чисел: ")
y = x.split()
print("Сумма списка: ", sumlist(y))
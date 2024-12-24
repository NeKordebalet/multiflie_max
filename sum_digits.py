def sum_digits(n):
    n = input("Введите число: ")
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
print("Сумма цифр: ", sum_digits(sum))
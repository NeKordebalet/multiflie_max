def temperature():
    celsius =float(input("Введите температуру: "))
    fahrenheit = (celsius * 1.8) + 32
    temp = fahrenheit
    return temp

print("Градусов по Фаренгейту: ", temperature())



if __name__ == '__main__':
    temperature()
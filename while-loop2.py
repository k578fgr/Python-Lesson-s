# Прибавляет числа до указанного с помощью цикла while
x = input("Enter a number to count to: ")
x = int(x)
y = 1

#Когда y станет больше x сработает команда break
while True:
    print(y)
    y = y + 1
    if y > x:
        break
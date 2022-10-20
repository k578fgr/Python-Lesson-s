# Различные типы данных

1. Целое число (Integer) - 1; 2; 3

2. Доброе число (Float) - 1.5; 2.3

3. Строка (String) - Входят буквы, цифры

4. Логические данные (Boolean) - True or False (Либо правда, либо нет)


Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0] on linux

Type "help", "copyright", "credits" or "license" for more information.
```
>>> type(98)
<class 'int'>
>>> type(98.6)
<class 'float'>
>>> type("Hello")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> 1Б2
  File "<stdin>", line 1
    1Б2
     ^
SyntaxError: invalid syntax
>>> 1<2
True
>>> 1>2
False
>>> 1=1
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> 1==1
True
>>> x = 3
>>> x * 5
15
>>> "Cisco" * x
'CiscoCiscoCisco'
>>> str1 = "Python"
>>> str2 = "Is"
>>> str3 = "Love"
>>> space = " "
>>> print(str1 + space +str2 + space + str3)
Python Is Love
>>> print(str1, str2, str3)
Python Is Love
>>> print (1, 2, 3)
1 2 3
>>> x = 3
>>> print("The value of x is " + x")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print("The value of x is " + str(x) )
The value of x is 3
>>> print("The value of x is ", x)
The value of x is  3

>>> num = 22/7
>>> print(num)
3.142857142857143

#В данном случае f означает format
#f-строка позволяет выполнять форматирование строки, подставлять переменные и т.д
#А в фигурных скобках можно передавать данные
>>> f"The value of num is {num}
  File "<stdin>", line 1

>>> f"The value of num is {num}"
'The value of num is 3.142857142857143'

#.2f означает что выводим только два символа
>>> pi = "{:.2f}".format(num)"
>>> f"The value of pi is {pi}."
'The value of pi is 3.14.'

# Работа со списками и словарями

Если открывается [] то это **список**

>>> hostnames = ["R1", "R2", "R3", "S1", "S2"]
#С помощью type узнаём кто такой hostnames
>>> type(hostnames)
<class 'list'>
#С помощью **len** можно узнать длинну этого списка
>>> len(hostnames)
5
#Вызовем весь список
>>> hostnames
['R1', 'R2', 'R3', 'S1', 'S2']

#Вызов первого значения. Идёт от нуля
>>> hostnames[0]
'R1'
#Значение минус идёт с конца поэтому S2
>>> hostnames[-1]
'S2'
#Здесь меняем первое значение(переопределили R1 на RTR1)
>>> hostnames[0] = "RTR1"
>>> hostnames
['RTR1', 'R2', 'R3', 'S1', 'S2']

#Удаляем третье значение от нуля (S1)
>>> del hostnames[3]
>>> hostnames
['RTR1', 'R2', 'R3', 'S2']
#Вложеные значение через двоеточия
>>> ipAddress = {"R1":"10.1.1.1", "R2":"10.2.2.1", "R3":"10.3.3.3"}
#dict это словарь
>>> type(ipAddress)
<class 'dict'>
>>> 
>>> ipAddress
{'R1': '10.1.1.1', 'R2': '10.2.2.1', 'R3': '10.3.3.3'}
#Обращаемся к R1
>>> ipAddress['R1']
'10.1.1.1'

>>> ipAddress["S1"] = "10.1.1.10"
#Обратим внимание что добавился в самый конец
>>> ipAddress
{'R1': '10.1.1.1', 'R2': '10.2.2.1', 'R3': '10.3.3.3', 'S1': '10.1.1.10'}

>>> ipAddress["R3"] = ["10.3.3.31", "10.3.3.2", "10.3.3.3"]
>>> ipAddress
{'R1': '10.1.1.1', 'R2': '10.2.2.1', 'R3': ['10.3.3.31', '10.3.3.2', '10.3.3.3'], 'S1': '10.1.1.10'}

# Функции ввода

>>> firstName = input("What is your first name?")
What is your first name? Kirill

>>> print("Hello" + firstName + "!")
Hello Kirill!
>>> 
```

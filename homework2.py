#Завдання 2.1
#Написати програму, яка просить користувача ввести 4-х значне число з клавіатури,
#після чого друкує на екрані стовпчик цифр, з якого це число складається.

#number = int(input('Enter a number: '))
#n1 = number // 1000
#n2 = number % 1000//100
#n3 = number % 100//10
#n4 = number % 10

#print(n1)
#print(n2)
#print(n3)
#print(n4)

#Завдання 2.2
# На запит від програми, користувач вводить 5-ти значне ціле, позитивне число.
# Вам необхідно "перевернути" цє число задом наперед,
# тобто щоб у результаті вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.

number = int(input('Enter a number: '))

n1 = number // 10000
n2 = number % 10000//1000
n3 = number % 1000//100
n4 = number % 100//10
n5 = number % 10

result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(result)
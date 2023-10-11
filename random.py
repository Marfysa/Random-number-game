import random
num1 = random.randint(1,100)
print("Добро пожаловать в числовую угадайку")
def is_valid(n):
    if n.isdigit:
        if 1 <= int(n) <= 100:
            return True
        else:
            return False
            


while True:
    a = input("Введите число от 1 до 100 ")
    if is_valid(a) == False:
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    else:
        break
while True:    
    if int(a) == num1:
        print("Вы угадали, поздравляем!")
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break
    elif int(a) > num1:
        print("Ваше число больше загаданного, попробуйте еще разок")
        a = int(input())
    else:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        a = int(input())

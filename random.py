import random
num1 = random.randint(1,100)
print("Добро пожаловать в числовую угадайку")
def is_valid(n):
    if n.isdigit:
        if 1 <= int(n) <= 100:
            return True
        else:
            return False
            
a = input("Введите число от 1 до 100")

while True:
    if is_valid(a) == False:
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    else:
        break

n = input()
print(is_valid(n))

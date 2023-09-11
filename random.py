import random
num1 = random.randint(1,100)
print("Добро пожаловать в числовую угадайку")
def is_valid(n):
    if n.isdigit:
        if 1 <= int(n) <= 100:
            return True
        else:
            return False

n = input()
print(is_valid(n))

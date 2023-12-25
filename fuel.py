""" exceptions """
try:
    x = int(input("Введите x: "))
    print(f"x = {x}")
except ValueError:
    print("x не целое число")

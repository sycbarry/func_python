
operators = '+', '-', '*', '/'

def f_get_number():
    return int(input("Enter and int: "))
def f_get_operator():
    return input("Get operator: ")
def f_calculate(n, o, n_1):
    return n+n_1 if operator == '+' \
        else n-n_1 if operator == '-' \
        else n/n_1 if operator == '/' \
        else n*n_1 if operator == '*' \
        else None

def f_main():
    return f_calculate(
        f_get_number(),
        f_get_operator(),
        f_get_number()
    )

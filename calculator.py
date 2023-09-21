from fastapi import FastAPI

my_app = FastAPI()
res = 0

@my_app.get("/")
def name():
    return {"калькулятор-обычный выполняет следующие действия: 1)сложение (+) 2)вычитание (-) 3)умножение (*) 4)деление (/) 5)возведение в степень (^)"}

@my_app.post("/")
def calculator(num1: int, operator: str,  num2: int):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        if num2!=0:
            return num1/num2
        else:
            return {"error"}
    elif operator == '^':
        return num1**num2
    else:
        return {"error"}

#Брезгунова А.Р. БВТ2303
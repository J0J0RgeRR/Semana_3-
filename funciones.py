def getSum(number1, number2):
    return number1 + number2

def showResult(result):
    return f"El resultado de {result}"

print("Dime un numero: ")
number1 = float(input())
print("Dime otro numero: ")
number2 = float(input())
result = getSum(number1, number2)
print(showResult(f"la suma es {result}"))
# Operações matemática
soma = 7 + 7
subtracao = 21 - 7
multiplicacao = 7 * 2
divisao = 28 / 2 # retorna um float
exponenciacao = 2 ** 4 # 2x2x2x2 

print("soma = ", soma)
print("subtração = ", subtracao)
print("multiplicação = ", multiplicacao)
print("divisão = ", divisao)
print("exponenciação = ", exponenciacao)

# o calculo da operação matematica é feita da esquerda para direita
# no python temos operações prioritárias a serem executadas
# ordem de prioridade
# ()
# **
# * /
# + -

print(3 * (3 + 3) / 3 - 3)

x = 5
print("x=5 result => ", x)
x += 3 # x = x + 3
print("x +=3 result => ", x)
x -= 3 # x = x - 3
print("x -=3 result => ", x)
x *= 3 # x = x * 3
print("x *=3 result => ", x)
x /= 3 # x = x / 3
print("x /=3 result => ", x)
x %= 3 # x = x % 3
print("x %=3 result => ", x)

#num_char = len(input("Whats your name? "))

# vai ocorrer um type error, pois não é possível concatenar string com inteiro
# print("your name has " + num_char + " characters.")

# checar o tipo da variável
# print(type(num_char))

# para converter para string
# new_num_char = str(num_char)

# agora que foi convertido é possível concatenar 
# print("your name has " + new_num_char + " characters.")

#########################################################

# convertendo o valor inteiro para float
a = float(123)
# verificando o tipo da variável
print(type(a))

# irá somar já que o valor em string está sendo convertido para float
print(70 + float("100.5"))

# irá concatenar já que os valores inteiros estão sendo convertidos para strings
print(str(20) + str(20))

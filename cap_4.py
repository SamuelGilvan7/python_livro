#4.2
velocidade = float(input("Informe a velocidade do carro:"))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Usuário multado!")
    print(f"O valor da multa será {multa}")
else:
    print("Não a nada!")    

#4.4
salario =  float(input("Informe o salário:"))
aumento = 0
if salario > 1.250:
    aumento = salario + (salario * 10/100)
    print(f"o valor do aumento será {aumento:7.2f}")
elif salario <= 1.250:
    aumento = salario + (salario * 15/100)
    print(f"O valor do aumento será {aumento:7.2f}")
 
#4.6
distancia = int(input("Informe a distância que irá pecorrer:"))
if distancia <= 200:
    dis_peercorrida = distancia * 0.50
    print(f"O valor da passagem será {dis_peercorrida}")
else: 
    dis_peercorrida = distancia * 0.45
    print(f"O valor da passagem será {dis_peercorrida}")

#4.10

print("Soma = 1")
print("Subtração = 2")
print("Divisão = 3")
print("Multiplicação = 4")
operacao = int(input("Informe a operação:"))
print("")
valor_1 = float(input("Informe o 1º número:"))
valor_2 = float(input("Informe o 2º número:"))

resultado = 0
if operacao == 1:
    resultado = valor_1 + valor_2
elif operacao == 2:
    resultado = valor_1 - valor_2
elif operacao == 3:
    resultado == valor_1/valor_2
elif operacao == 4:
    resultado = valor_1 * valor_2
else:
    print("Tente novamente!")    

print(f"Resultado: {resultado}")





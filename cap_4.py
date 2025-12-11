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

#4.11
valor_casa = float(input("Informe o valor da casa:"))
salario_valor = float(input("Informe o seu salário:"))
qnt_anos = int(input("Anos:"))

#Prestação relação valor casa/anos

prestacao = valor_casa / (qnt_anos * 12)
if prestacao > (salario_valor * 30/100):
    print("Empréstimo NEGADO!")
else: 
    print("Empréstimo APRAVADO!") 

#4.12
print("CATEGORIA")
print("R -- RESIDÊNCIAS")
print("I -- INDÚSTRIAS")
print("C -- COMÉRCIO")


qnt_kwh = int(input("Quantidade de KWH:"))
cat =  (input("informe sua categoria:"))
nova_cat = cat.upper()

valor_pago = 0

if nova_cat == "R":
    if qnt_kwh <= 500:
        valor_pago = 0.40 * qnt_kwh
    else:
        valor_pago = 0.65 * qnt_kwh
elif nova_cat == "C":
    if qnt_kwh <= 1000:
        valor_pago = 0.55 * qnt_kwh
    else:
        valor_pago = 0.60 * qnt_kwh
elif nova_cat == "I":
    if qnt_kwh <= 5000:
        valor_pago = 0.55 * qnt_kwh
    else:
        valor_pago = 0.60 * qnt_kwh        
else:
    print("Digite a CATEGORIA CORRETA!")        

print(f"A sua categoria {nova_cat} e o valor a ser pago será R${valor_pago:7.2f}")




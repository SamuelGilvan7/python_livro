
#5.6
tabela = int(input("Tabuada de:"))

x = 0

while x <= 10:
    print(f"{tabela} x {x} = {tabela * x}")
    x += 1

#5.7  
n = int(input("Tabuada de: "))
inicio = int(input("De: "))
fim = int(input("Até: "))

x = inicio 

while x <= fim:  
    print(f"{n} x {x} = {n * x}")
    x = x + 1  

#5.8
num_1 = int(input("Informe o 1º valor:"))
num_2 = int(input("Informe o 2º valor:"))

cont = 0
x = 0
while cont < num_2:
    x += num_1
    cont += 1 

print(f"{num_1} x {num_2} = {x}")


#5.9
a = int(input("Informe o 1º valor:"))
b = int(input("Informe o 2º valor:"))

div = 0
resto = a

while b <= a:
    resto -= b
    div += 1

print(f"A divisão inteira de {a} por {b} é {div} com resto {resto}")        

#5.10
pontos  = 0 
questao = 1 

while questao <= 3:
    resposta = input(f"Resosta da questão {questao}: ")
    nova_resposta = resposta.upper()
    if questao == 1 and nova_resposta == "B":
        pontos += 1
    if questao == 2 and nova_resposta == "A":
        pontos += 1
    if questao == 3 and nova_resposta == "D":
        pontos += 1
    questao += 1 

print(f"O aluno fez {pontos} ponto(s)")

#5.11
deposito_inicial = float(input("Informe o depósito inicial:"))
taxa_de_juros = float(input("Informe a taxa de jutos:"))

total = deposito_inicial
juros_total = 0
c = 1

while c <= 24:

    taxa_de_juros = deposito_inicial * (taxa_de_juros * 100)
    juros_total += taxa_de_juros 
    total +=  deposito_inicial
    print(f"{c} mês {total} ")

    c += 1
print(f'O valor total foi R${total:7.2f} total de juros R${juros_total:7.2f}')


#5.12
deposito_inicial = float(input("Informe o depósito inicial:"))
taxa_de_juros = float(input("Informe a taxa de juros:"))
valor_mensalmente = float(input("Informe o valor que será depositado mensalmente:"))

total = deposito_inicial
juros_total = 0
c = 1

while c <= 24:
    total += valor_mensalmente
    
    juros = total * (taxa_de_juros / 100)
    juros_total += juros 
    total +=  juros

    print(f"{c}º mês - R${total:7.2f} ")
    

    c += 1

print(f'O valor total será de {total:7.2f} o total de juros foi R${juros_total:7.2f}')   

#5.13

valor_inicial_divida = float(input("Informe o valor inicial da dívida:\n"))
juros_mensal = float(input("Informe o valor do juros mensal (%):\n"))
valor_mensal_pago = float(input("Informe o valor que será pago mensalmente:\n"))

juros_total_pago = 0
valor_inicial_t = valor_inicial_divida
total_pago_mensal = 0
meses = 0

while valor_inicial_t > 0:
    juros_mensal_calculado = valor_inicial_t * juros_mensal / 100
    juros_total_pago += juros_mensal_calculado

    valor_inicial_t += juros_mensal_calculado
    valor_inicial_t -= valor_mensal_pago

    total_pago_mensal += valor_mensal_pago
    meses += 1

print(f"O total de meses necessários para quitar a dívida será de {meses}")
print(f"O valor total pago será de R$ {total_pago_mensal:.2f}")
print(f"O total de juros pago foi de R$ {juros_total_pago:.2f}")

#5.14
soma = 0
c = 0
while True:
    valor = int(input("Informe o valor(Para sair 0)"))
    c += 1 
    soma += valor
    if valor == 0:
        break
print(f"O valor total será de {soma} e foram digitados {c-1} números!")
print(f"A média será {int(soma / (c-1))}")    


#5.15
print ("""
Código | Preço
   1   | 0.50
   2   | 1.00
   3   | 4.00
   5   | 7.00
   9   | 8.00 
   0   | Sair               
""")
total = 0
while True:
    cod = int(input("Informe o código:"))
    preco = 0
    if cod == 0:
        break
    qnt = int(input("A quantidade:"))

    if cod == 1:
        preco = 0.50
    elif cod == 2:
        preco = 1.00
    elif cod == 3:
        preco = 4.00
    elif cod == 5:
        preco = 7.00
    elif cod == 9:
        preco = 8.00 
    else: 
        print("Código inválido")
    if preco != 0:
        apagar = apagar + (preco * qnt)
print(f"Total a pagar R${total:8.2f}")

#5.18
valor = int(input("Digite o valor a pagar:"))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1 
    else:   
        print(f"{cedulas} cédula(s) de R${atual}") 
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1     
        cedulas = 0                


#5.19
valor = int(input("Digite o valor a pagar:"))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1 
    else:   
        print(f"{cedulas} cédula(s) de R${atual}") 
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.02:
            atual = 0.01       
        cedulas = 0    
        
#5.21
while True:
    valor = int(input("Digite o valor a pagar(0 para sair):"))
    if valor == 0:
        break
    cedulas = 0
    atual = 100
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1 
        else:   
            print(f"{cedulas} cédula(s) de R${atual}") 
            if apagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1     
            cedulas = 0                
#5.22

while True:
    print ("""
        Código | Preço
        1   | Subtração
        2   | Adição
        3   | Multiplicação
        4   | Divisão
        5   | Sair               
    """)
    cod = int(input("Informe o código:"))
    if cod == 5:
        print("Saindo...")
        break
    elif cod >= 1 and cod<=5:
        n = int(input("Tabuada de:"))
        x = 1   
        while x <= 10:   
            if cod == 1:
                print(f"{n} + {x} = {n + x}")
            elif cod == 2:
                print(f"{n} - {x} = {n - x}")
            elif cod == 3:
                print(f"{n} / {x} = {n / x:5.4f}")
            elif cod == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida!")
#5.23
num_primo = int(input("Informe o valor:"))
if num_primo == 0 or num_primo == 1:
    print("O valor são números especias!")
elif num_primo == 2:
    print(f"O {num_primo} é único número par primo!")
elif num_primo % 2 == 0:
    print(f"O {num_primo}  não é primo!")
else:
    prox_primo = 3
    primo = True
    while prox_primo < num_primo:
        if num_primo % prox_primo == 0:
            primo = False
            break
        prox_primo += 2
    if primo:
        print(f"O número {num_primo} é primo!")
    else:
        print(f"O número {num_primo} não é primo!")   
#5.24
qnt_primos = int(input("Informe a quantidade de primos:\n"))
if qnt_primos == 1:
    print("2")
elif qnt_primos <= 0: 
    print("Valor inválido ")
else:
    print("2")
    primo_atual = 3
    num = 2
    while num < qnt_primos:
        impar = 3
        while impar < primo_atual:
            if primo_atual % impar == 0:
                break
            impar += 2
        if impar == primo_atual:
            print(primo_atual)
            num += 1
        primo_atual += 2 
        



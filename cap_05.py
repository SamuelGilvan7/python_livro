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

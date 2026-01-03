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
        

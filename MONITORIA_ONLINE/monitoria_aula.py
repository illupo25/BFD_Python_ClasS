soma = 0
while True:
    num = input("Informe os numeros para somar (0 finaliza a soma): ")
    if num.isalpha():
        print("informe os numeros")
        continue
    if num == "0":
        break
    soma += float(num)
print(soma)



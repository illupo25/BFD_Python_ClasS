lista1 = []
for i in range(10):
            lista1.append(i*2)
print(lista1)

lista2 = [i*2 for i in range(3) if i%2 == 0]
print(lista2)
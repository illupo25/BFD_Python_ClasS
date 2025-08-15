frutas = ["banana", "manga", "laranja", "jaca", "melao"]

salada_de_frutas = frutas

# print(frutas)
# print(salada_de_frutas)
# salada_de_frutas.append("melao")
# print("---")
# print(id(frutas))
# print(id(salada_de_frutas))
# print("---")
# print(id(frutas))
# print(id(salada_de_frutas))

#print(frutas[:])
#print(frutas)
temperos = ["pimenta", "sal"]
#frutas += temperos
#frutas.insert(5, "limao")
#frutas.append("jaca")
#fruta = "manga"

## REMOVER ITENS
#del frutas[1]
#pop
#remove
#clear

#print(sorted (frutas))
#frutas.sort()
#frutas.sort(reverse=True)
#print(frutas)

fruta = "morango"

morango_do_amor = fruta

# print(id(fruta))
# print(id(morango_do_amor))

### COPIAR LISTA
# salada_de_frutas = frutas.copy()
# for fruta in frutas:
#     salada_de_frutas.append(fruta)

#     print(frutas)
#     print(salada_de_frutas)

# print(id(frutas))
# print(id(salada_de_frutas))

#print(frutas.count("jaca"))
salada_de_frutas = ["maca"]
print(frutas)
# print(frutas.index("melao"))
idx_melao = frutas.index("melao")
frutas.pop(idx_melao)
print(frutas)


#String simples
print("Olá mundo \n")

#Printando variável
variavel = "String \n"
print(variavel)

#Outra forma seria
print(f'{variavel}')

#ou por exemplo
print("{}".format(variavel))


#Printando uma parte da String
print(variavel[2])


#Printando o último caracter
print(variavel[-1], "\n")


#Printando a string reversa
print(variavel[::-1])


#Printando uma variável extensa 
variavel_grande = """esse é um texto bem grande, 
como você pode perceber,
ele tem várias linhas,
mas mesmo assim conseguimos mostrar tranquilamente \n"""
print(variavel_grande)


#Podemos usar loopings em uma string também
for item in variavel:
    print(item)




#Podemos também fazer uma verificação
print("g" in variavel)

#ou 
if "g" in variavel:
    print("Sim tem um 'g' alí")

#ou
if  "x" not in variavel:
    print("Não tem um 'x' alí ")
    



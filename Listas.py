#Criando listas 
# OBS: As listas em Python começam com o índice em 0
##Primeira forma
Lista = [1,2,6,4,3,2,1,0,4,5,6]

Lista_2 = list((1,2,3,4,5,6)) #Aqui estamos transformando uma tupla em uma lista

Lista_3 = ["abc", 34, True, 40, "male"]


#E se tentarmos multiplicar uma variável em lista? 
Lista_4 = Lista * 2 
# Ele acaba duplicando os valores da lista e adicionando a mesma lista ao final

#podemos Ordernar facilmente uma lista
Lista.sort()
print(Lista)


#Podemos reverter a ordem também
Lista.sort( reverse= True)
print("Reversa ",Lista)

#Adicionando um novo item na lista
Lista.append("Novo item")
print(Lista)

#Removendo item da lista
Lista.pop()
print(Lista)

#Podemos escolher qual item também vai ser deletado
#Nesse caso estamos retirando o número 5 que está no índice 2  da lista
Lista.pop(2)
print(Lista)

#Outra forma de remover
Lista_5 = [1,2,3,4,5] #Criando uma nova lista
print("Antes",Lista_5)
print("O item que vamos tirar",Lista_5[2]) 
del Lista_5[2]
print("Depois",Lista_5)


#Alterando o valor de um item
Lista_6 = [1,2,3,4,5] #Criando uma nova lista
print("Antes",Lista_5)
print("O item que vamos alterar",Lista_5[2]) 
Lista_5[2] = 9
print("Depois",Lista_5)



#Concatenando listas
Lista_7 = Lista_5 + Lista_6
print(Lista_7)



#Importar biblioteca
import math

#Declarar algumas variáveis
nome = input('Qual é o seu nome? ') #Seu nome
twitterUser = input('Qual seu usuário no twitter? ') #Seu usuário no twitter
numA = int(input('Diga um número que você gosta: ')) #Um número que você gosta
numB = int(input('Diga outro número que você gosta: '))#Outro número que você gosta

#Realizar operações matemáticas
soma = numA+numB #Soma de numA + numB
subt = numA-numB #Subtração de numA - numB
div = numA/numB #Divisão de numA/numB
mul = numA*numB #Multiplicação de numA*numB
pot = numA**numB #Potenciação de numA por numB
raiz = math.sqrt(numB) #Radiciação de numB

#Realizar uma operação de concatenação
concat = nome + ' ' + twitterUser

#Exibir esses resultados no terminal
print("Olá! ",nome, ". Seu usuário do twitter é: ", twitterUser)
print("Seja bem vindo!")
print("Você escolheu os números: ", numA, " e ", numB)
print("São ótimos números! Veja só o resultados das operações com eles! ")
print("Soma: ",soma)
print("Subtração: ",subt)
print("Divisão: ",div)
print("Multiplicação: ",mul)
print("Potenciação: ",pot)
print("Raiz: ",raiz)
print("Concatenação: ",concat)


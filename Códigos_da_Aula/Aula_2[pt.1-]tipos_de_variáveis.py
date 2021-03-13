#receber valores variáveis
nome = 'João' #variável tipo texto
idade = float(25) #variável tipo inteiro
altura = str(1.86) #variável tipo decimal
programador = True #variável booleana

#reconhecer o tipo <class> de cada variável
tipoNome = type(nome) #identificando o tipo da variável nome
tipoIdade = type(idade) #identificando o tipo da variável idade
tipoAltura = type(altura) #identificando o tipo da variável altura
tipoProgramador = type(programador) #identificando o tipo da variável programador

#exibir o valor de cada variável, seguido do tipo da variável
print(nome,tipoNome)
print(idade,tipoIdade)
print(altura, tipoAltura)
print(programador, tipoProgramador)

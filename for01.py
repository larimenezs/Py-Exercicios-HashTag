#Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hote, os hóspedes podem ter quartos com 1, 2, 3, 4 pessoas.Seu sistema deve conseguir: 

#1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto.
#2. De acordo com a quantidade de pessoas do hóspede, deve fazer um for para perguntar o nome e o cpf de cada pessoa, a fim de registrá-la no quarto.
#3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome e o cpf da pessoa.


qnt_pessoa = int(input('Quantos hóspedes vão ficar no quarto? '))
quarto = []


for p in range(qnt_pessoa):
    nome = str(input('Qual o nome do hóspede? '))
    cpf = int(input('Qual é o cpf do hóspede? '))
    hospede = [nome, f'cpf: {cpf}']
    quarto.append(hospede)
print(quarto)
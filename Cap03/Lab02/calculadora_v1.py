# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("Selecione o número da operação desejada:")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")

print("4 - Divisão")

opcao = int(input("Digite sua opção (1/2/3/4): "))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


if opcao == 1:
	print("%s + %s = %s" %(num1,num2,num1+num2))
elif opcao == 2:
	print("%s - %s = %s" %(num1,num2,num1-num2))
elif opcao == 3:
	print("%s * %s = %s" %(num1,num2,num1*num2))
elif opcao == 4:
	print("%s / %s = %s" %(num1,num2,num1/num2))
else:
	print("Opção inálida!")


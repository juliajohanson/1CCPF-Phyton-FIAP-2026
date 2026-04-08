num = int(input("Digite o número para receber a tabuada: "))


for i in range(0, 26): # i é um contador que vai aumentando ate chegar no 2 numero (26)
    resultado = num * i # multiplica o numero do usuario vezes o contador (ex: x 1, 2, 3 ,4...)
    print(f"{num} x {i} = {resultado}")
    # printa o resultado de cada operação, fazendo um loop do 0 até o ultimo numero
    # ele realiza o calculo, printa, aumenta o contador e e repete até o 25
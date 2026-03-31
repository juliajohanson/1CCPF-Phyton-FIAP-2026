# estruturas condicionais if else

nota_final = 3

if nota_final < 4:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

print("fim")

# estruturas condicionais elseif

nota_final = 6

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")
numero_base = int(input("Digite um numero:"))
numero_p5 = numero_base % 5
numero_p3 = numero_base % 3
if numero_p3 + numero_p5 == 0:
    print("O número é compativel!")
else:
    print("O número é incompativel!")
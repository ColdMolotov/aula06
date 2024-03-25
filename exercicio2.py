compra = float(input("Digite o valor da compra: "))
desconto10 = (compra / 100) * 10
desconto20 = (compra / 100) * 20
desconto30 = (compra / 100) * 30

if compra <= 1000.0:
    valor_pago = compra - desconto10
    print("Você pagou R$:", valor_pago, "Com um desconto de R$", desconto10)
elif 5000.0 >= compra > 1000.0:
    valor_pago = compra - desconto20
    print("Você pagou R$:",valor_pago, "Com um desconto de R$",  desconto10)
elif compra > 5000.0:
    valor_pago = compra - desconto30
    print("Você pagou R$:",valor_pago, "Com um desconto de R$",  desconto30)

largura = float(input("digite a largura do cômodo: "))
comprimento = float(input("digite o comprimento do cômodo: "))
altura = 2.80
porta = 0.80 * 2.10
parede_comp = comprimento * altura
parede_larg = largura * altura
tamanho_total = (parede_larg * 2) + (parede_comp * 2) - porta
qtd_litros = tamanho_total / 3
litros = float(input("Digite quantos litros (L) suas latas de tinta tem: "))
lataP = 1 / litros
qtd_lp = qtd_litros / lataP
lataM = 3.7 / litros
qtd_lm = qtd_litros / lataM
lataG = 18 / litros
qtd_lg = qtd_litros / lataG
if litros == 1:
    print("você precisará de ", qtd_lp, "latas de tinta")
elif litros == 3.7:
    print("você precisará de ", qtd_lm, "latas de tinta")
elif litros == 18:
    print("você precisará de ", qtd_lg, "latas de tinta")



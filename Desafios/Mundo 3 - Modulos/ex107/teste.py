import moeda
# from ex107 import moeda

p = float(input('Digite o preço: R$ '))
t = float(input('Digite a taxa(%):  '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p):.2f}.')
print(f'O dobro de R${p} é R$ {moeda.dobro(p):.2f}.')
print(f'Aumentando {t} % temos R$ {moeda.aumentar(p, t):.2f}.')
print(f'Diminuindo {t} % temos R$ {moeda.diminuir(p, t):.2f}.')
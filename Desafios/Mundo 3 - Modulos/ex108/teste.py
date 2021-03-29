import moeda
# from ex107 import moeda

p = float(input('Digite o preço: R$ '))
t = float(input('Digite a taxa(%):  '))
print(f'A metade de {moeda.moedaFormat(p)} é {moeda.moedaFormat(moeda.metade(p))}.')
print(f'O dobro de {moeda.moedaFormat(p)} é {moeda.moedaFormat(moeda.dobro(p))}.')
print(f'Aumentando {moeda.taxaFormat(t)} temos {moeda.moedaFormat(moeda.aumentar(p, t))}.')
print(f'Diminuindo {moeda.taxaFormat(t)} temos {moeda.moedaFormat(moeda.diminuir(p, t))}.')
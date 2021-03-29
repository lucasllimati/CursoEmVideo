import moeda
# from ex107 import moeda

p = float(input('Digite o preço: R$ '))
t = float(input('Digite a taxa(%):  '))
print(f'A metade de {moeda.moedaFormat(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moedaFormat(p)} é {moeda.dobro(p, True)}.')
print(f'Aumentando {moeda.taxaFormat(t)} temos {moeda.aumentar(p, t, True)}.')
print(f'Diminuindo {moeda.taxaFormat(t)} temos {moeda.diminuir(p, t, True)}.')

# help(moeda.metade)
# help(moeda.dobro)
# help(moeda.aumentar)
# help(moeda.metade)
# help(moeda.diminuir)
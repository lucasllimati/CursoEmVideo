# 62
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('\33[32mGerador de PA\33[m')
print('=+'*10)

# Description
# p ~> first term
# r ~> reason
# t ~> term
# c ~> counter
# termos ~> initial amount of terms
# novotermo ~> additional amount of terms
# total ~> total terms

p = int(input('Primeiro termpo: '))
r = int(input('Razão da PA: '))
t = p
c = 0
termos = 10
novotermo = 1
total = termos

while novotermo != 0:
    while c < termos:
        print('{}'.format(t), end=' → ')
        t += r
        c += 1
    print('\33[33mPAUSA\33[m')
    novotermo = int(input('\nQuantos termpo você quer mostrar a mais? '))
    if(novotermo < 0):
        print('\33[31Valor inválido!\33[m')
        novotermo = 0
    else:
        termos += novotermo
    total += novotermo
print('Progressão finalizada com {} termos mostrador'.format(total))
print('\33[31mFIM\33[m')
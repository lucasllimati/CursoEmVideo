# EXERCÍCIO 14
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Informe a temperatura em °C: '))

fahrenheit = celsius * 1.8000 + 32
kelvin = celsius + 273.15

print('A temperatura de {:.2f} °C corresponde a {:.2f} °F e {:.2f} K.'.format(celsius, fahrenheit, kelvin))

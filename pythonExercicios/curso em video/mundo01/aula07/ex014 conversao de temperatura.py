print('\n'
      '\n'
      '==================================================\n'
      'Escreva um programa que converta uma temperatura\n'
      'digitada em ºC e converta para ºF\n'
      '==================================================\n'
      '')
####################################################################################
####################################################################################
#    Celsius > Fahrenheit - ºF = ºC * 1.8 + 32
# Fahrenheit > Celsius ---- ºC = (ºF - 32) / 1.8
#    Celsius > Kelvin ----- ºK = ºC + 273.15
#     Kelvin > Celsius ---- ºC = ºK - 273.15

c = float(input('Quantos graus Celsius? '))

f = c * 1.8 + 32

print('\n'
      f'{c}ºC equivale a {f:.1f}ºF')

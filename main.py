#----------------------------------------------------------------------------
#TERCEIRO CÓDIGO

qtde = int(input('Informe Quanto Cigarros você fuma por dia: '))
anos = int(input('Informe por quantos anos você fuma: '))

soma = qtde*(anos*365)
minutos = soma*10

subtrai = (minutos/60)/24

print('Você tem %.2f dias a menos de vida' %subtrai)


#---------------------------------------------------------------------------
#SEGUNDO CÓDIGO

print('----Calculadora de Dias de Carro----')

d = int(input('Quanto Dias o Carro Ficou Alugado: '))
k = float(input('Quanto Km foram rodados: ').replace(',','.'))

paga=(d*60)+(k*0.15)

print('O valor a ser pago é R${:.2f} devido a {:.0f} dias de aluguel e {:.0f} Km rodados '.format(paga,d,k))


#---------------------------------------------------------------------------
#PRIMEIRO CÓDIGO

print('----Conversor Temperatura Celsius para Farenheit----')

c = float(input('Insira a temperatura em Celsius: ').replace(',','.'))
f = (9*(c/5)+32)
print('Farenheit : {:.2f}'.format(f))

print('\n\n----Conversor de Temperatura Farenheit para Celsius----')

f = float(input('insira a temperatura em Farenheit: ').replace(',','.'))
c = ((f-32)/1.8)
print('Celsius : {:.2f}'.format(c))
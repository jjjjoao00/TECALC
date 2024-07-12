import math

print("Calculadora de madeiramento para telhado de duas águas")


lado_maior = float(input('digite a dimensão do maior lado, em metros = '))
lado_menor = float(input('digite a dimensão do menor lado, em metros = '))
inclinacao = float(input('digite a inclinacao da telha (sem sinal de %) '))
espaçamento_terca = float(input('Digite o espaçamento entre as terças, em metros = '))
espaçamento_caibro = float(input('Digite o espaçamento entre os caibros, em metros = '))
espaçamento_ripa = float(input('Digite o espaçamento entre as ripas, em metros = '))
beiral = float(input('Digite o tamanho do beiral, em metros = '))



#CALCULO QUANTIDADE DE CAIBROS

#ALTURA TOTAL DO TELHADO COM O BEIRAL 
def altura_telhado_beiral ():
    return ((lado_maior/2) + beiral)* (inclinacao/100)

#COMPRIMENTO TOTAL DOS CAIBROS (HIPOTENUSA)
def hipotenusa ():
    return math.sqrt((altura_telhado_beiral()**2) + (((lado_maior/2)+beiral)**2))

#QUANTIFICAÇÃO DOS CAIBROS, MULTIPLICANDO PELO PANO DE COBERTURA (DUAS ÁGUAS)
def qtd_caibro ():
    return (round((lado_menor + (beiral*2)) / espaçamento_caibro)) * 2

#CALCULO QUANTIDADE DE TERÇAS
def qtd_terça(): 
    return (round((lado_maior/2) / espaçamento_terca) * 2) + 1

#CALCULO QUANTIDADE DE RIPAS, MULTIPLICADO PELO PANO DE COBERTURA (DUAS ÁGUAS)
def qtd_ripa():
    return (round((hipotenusa() / espaçamento_ripa) + 1) * 2)

#CALCULO ALTURA DA CUMEEIRA
def altura_cumeeira():
    return (inclinacao/100) * (lado_maior/2)


#VARIAVEIS INTERMEDIARIAS
resultado_cumeeira = altura_cumeeira()
resultado_hipotenusa = hipotenusa()



print('A altura da cumeeira é de: ' + "{:.2f}".format(resultado_cumeeira) + ' cm')
print('O número de terças para o telhado é de: ', qtd_terça(), "und com "+ "{:.2f}".format(lado_menor + (beiral*2)) + ' m de comprimento cada')
print('O numero de caibros para o telhado é de: ' , qtd_caibro(),' und com '+ "{:.2f}".format(resultado_hipotenusa) + ' m de comprimento cada')
print('O número de ripas para o telhado é de: ',qtd_ripa()," und com "+ "{:.2f}".format(lado_menor + (beiral*2)) + ' m de comprimento cada')

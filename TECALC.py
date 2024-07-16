# -*- coding: utf-8 -*-
import csv
import math

print("Calculadora de estrutura usual de cobertura, madeira e telha cerâmica")


lado_maior = float(input('digite a dimensão do maior lado, em metros = '))
lado_menor = float(input('digite a dimensão do menor lado, em metros = '))
inclinacao = float(input('digite a inclinacao da telha (sem sinal de %) '))
espaçamento_terca = float(input('Digite o espaçamento entre as terças, em metros = '))
espaçamento_caibro = float(input('Digite o espaçamento entre os caibros, em metros = '))
espaçamento_ripa = float(input('Digite o espaçamento entre as ripas, em metros = '))
beiral = float(input('Digite o tamanho do beiral, em metros = '))
telhas_m2 = float(input('Digite a quantidade de telhas por m2: '))



#CAMADA DE SERVIÇO

#QUANTITATIVOS SIMPLES 

def area_telhado():
    return (lado_maior + beiral) * (lado_menor + beiral)

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

#LADO MENOR MAIS BEIRAL *2
def lado_menor_():
    return lado_menor + (beiral*2)

#QUANTIFICAÇAO DE TELHAS UNITARIO

#FATOR DE CORREÇÃO
...
match inclinacao:
        case 5.00:
            fator_ = 1.001
        case 10.00:
            fator_ = 1.005    
        case 15.00:
            fator_ = 1.011    
        case 20.00:
            fator_ = 1.020    
        case 25.00:
            fator_ = 1.031    
        case 30.00:
            fator_ = 1.044    
        case 35.00:
            fator_ = 1.059    
        case 40.00:
            fator_ = 1.077    
        case 45.00:
            fator_ = 1.097    
        case 50.00:
            fator_ = 1.118    
        case _:
            print ("Inclinação não definida no banco de dados")

#ÁREA COBERTA PELAS TELHAS
def area_corrigida():
    return area_telhado() * fator_

#QUANTIDADE UNITARIA DE TELHAS (CONSUMO)
def consumo_por_m2_telhas():
    return area_corrigida()*telhas_m2

# def qtd_pregos():
#     return (480 * area_corrigida())

#VARIAVEIS INTERMEDIARIAS
resultado_cumeeira = altura_cumeeira()
resultado_hipotenusa = hipotenusa()
resultado_lado_menor = lado_menor_()
resultado_area_corrigida = area_corrigida()

#================================================================================


#SAÍDAS

#TEXTO NO TERMINAL
print('A altura da cumeeira é de: ' + "{:.2f}".format(resultado_cumeeira) + ' cm')
print('O número de terças para o telhado é de: ', qtd_terça(), "und com "+ "{:.2f}".format(resultado_lado_menor) + ' m de comprimento cada')
print('O numero de caibros para o telhado é de: ' , qtd_caibro(),' und com '+ "{:.2f}".format(resultado_hipotenusa) + ' m de comprimento cada')
print('O número de ripas para o telhado é de: ',qtd_ripa()," und com "+ "{:.2f}".format(resultado_lado_menor) + ' m de comprimento cada')
print('O consumo de telhas para o seu telhado é de: ', round(consumo_por_m2_telhas()),  ' por m2')


#EXPORTAÇÃO PARA CSV (PLANILHA)
with open('./RELATORIO_MADEIRAMENTO.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(['Altura da cumeeira ',' ', ' ', "{:.2f}".format(resultado_cumeeira) ,' m' ])
    writer.writerow(['Numero de terças ', qtd_terça(), 'Comprimento ', "{:.2f}".format(resultado_lado_menor), ' m' ])
    writer.writerow(['Numero de caibros ', qtd_caibro(),'Comprimento ', "{:.2f}".format(resultado_hipotenusa), ' m'])
    writer.writerow(['Numero de ripas ', qtd_ripa(), 'Comprimento ', "{:.2f}".format(resultado_lado_menor), ' m'])
    writer.writerow (['O consumo de telhas para o seu telhado é de: ', round(consumo_por_m2_telhas()),  ' por m2'])
#EXIBE O CSV NO TERMINAL
with open('./RELATORIO_MADEIRAMENTO.csv') as csvfile:
    leitor = csv.reader(csvfile) 
    for x in leitor:
        print(x)    

#================================================================================



#TODO 
#FORMATAÇÃO DA SAÍDA DO CSV
#CALCULO E DIMENSIONAMENTO DAS TESOURAS
#QUANTIFICAÇÃO DE PREGOS E PARAFUSOS (KG)
#QUANTIFICAÇÃO DA COMPOSIÇÃO SINAPI (COBERTURA)
#SELEÇÃO DE TELHAS, DEFINIÇÃO DOS PARÂMETROS CARACTERÍSTICOS DELAS
#DIMENSIONAMENTO DAS SEÇÕES DAS PEÇAS (TERÇAS, CAIBROS, RIPAS), SE NECESSÁRIO
#CALCULO DO PESO TOTAL DA ESTRUTURA DO TELHADO + TELHAMENTO (MOLHADO) + PREGOS/PARAFUSOS
#CALCULO DE TRANSMITÂNCIA TÉRMICA (DEFININDO UMA ZONA AMBIENTAL)
#APRESENTAR OPÇÕES PARA UM MELHOR CUSTO X BENEFICIO (PESO DE ESTRUTURA(TELHAS) E TRANSMITÂNCIA TÉRMICA)
#GERAR O RELATÓRIO COMPLETO EM CSV

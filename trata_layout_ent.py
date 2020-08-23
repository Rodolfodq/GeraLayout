import os
import sys
from dicionario_ent import dicio_letras, dicio_palavras

def le_texto(arquivo):
    dict_aux = {}
    #aux_str = ''
    try:
        with open(arquivo, 'r', encoding="utf-8") as texto:
            readtexto = texto.readlines()
            texto.close                  
        for linha in readtexto:
            aux_str = ''
            separate = (linha.split())        
            for i in range(len(separate)-1):                                         
                aux_str += (separate[i])
            nome_campo = corrige_caracter(aux_str)
            nome_campo = altera_nome_campo(nome_campo)            
            dict_aux[nome_campo] = separate[-1]
    except:
        print("Arquivo inválido.")                                  
    return(dict_aux)

def corrige_caracter(campo):    
    novo_campo = ''     
    for indice in dicio_letras:
        for i in range(len(dicio_letras[indice])):
            letra = (dicio_letras[indice][i])
            for item in campo:                
                if letra == item:            
                    novo_campo += indice                    
                else:
                    novo_campo += item                    
            campo = novo_campo
            novo_campo = ''        
    return campo

def altera_nome_campo(campo):
    novo_campo = ''     
    for indice in dicio_palavras:
        for i in range(len(dicio_palavras[indice])):
            palavra = (dicio_palavras[indice][i])
            if palavra in campo:
                novo_campo = campo.replace(palavra, indice)
        if novo_campo != '':
            campo = novo_campo
            novo_campo = '' 
    return campo


def salva_lay_entrada(texto, arq_name):
    arq_name = "L" + arq_name + ".ent"
    str2 = ''
    for linha in texto:
        str3 = ''
        str3 = linha + ';' + texto[linha] + ';;' + '\n'
        str2 = str2 + str3
    try:
        with open(".\\Entrada\\" + arq_name, 'w', encoding="utf-8") as arquivo:        
            arquivo.write(str2)
            print("Aqruivo {} salvo com sucesso.".format(arq_name))
    except:
        print("Algo deu errado ao salvar o arquivo.")
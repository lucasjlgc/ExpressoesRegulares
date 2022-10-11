#Estas aulas são baseadas no curso do professor Otavio Miranda

#AULA001
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re


#findall: Encontra todas as ocorrencias do padrão no meu texto
#Search: Encontra a primeira ocorrencia e retorna o objeto match com a primeira posição;
#Sub: Substitui algo dentro do meu texto
#Compile: Compila expressões regulares. No caso de precisar reutilizar a expressão regular e 
#esta for muito complexa.

string = "Este é um teste de expressões teste regulares"
print(re.search(r'teste',string)) #r evita que utilizemos muitas \\\\ para escapar um character

print(re.findall(r'teste',string)) #Irá me retornar uma lista com as palavras padrão que existem na string

print(re.sub(r'teste','ABCD',string)) #No segundo parametro é a palavra que irá substituir

print(re.sub(r'teste','ABCD',string, count=1)) #Count= 1, substitui apenas a primeira palavra por ABCD

#Compilando minha expressão regular
print("\n--------------\n")
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF',string))


--------------------------------------""--------------------------------------------------------
#AULA002

#import re (Já foi importanto no primeiro código)

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

texto = """ 

João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!

"""

print(re.findall(r'João|Maria|adultos', texto))
print(re.findall(r'João|Maria|ad.ltos', texto)) #O ponto é qualquer caracteres
print(re.findall(r'[Jj]oão|Maria|adultos', texto)) #[] é um conjunto de caracteres que determinamos
print(re.findall(r'[a-z]oão|Maria|adultos', texto)) #[a-z] Qualquer letra entre "a" até "z"
print(re.findall(r'[A-Z]oão|Maria|adultos', texto)) #[a-z] Qualquer letra entre "a" até "z" MAIUSCULO 
print(re.findall(r'jOãO|Maria|adultos', texto,flags=re.I)) #A flag re.I ignora o fato de ser MAIUSCULO ou minisuculo e retorna a palavra


--------------------------------------""--------------------------------------------------------
#AULA003

# Meta caracteres: . ^ $ ( )

#--Quantificadores: São aplicados à esquerda do charactere que sera usado.
# * = zero ou n vezes
# + = 1 ou n vezes
# ? 0 ou 1 vez
#{min, max} = minimo ou maximo de vezes
#{n} = Numero especifico de vezes
#------Exemplos------#
#{10,} 10 ou mais
#{,10} de Zero a 10
#{10} especificamente 10
#{5,10} de 5 a 10 vezes
#()+ [a-zA-Z0-9]+ = Pega uma letra entre a-z, porém se tiver o sinal de + pega todas as letras existentes entre a-z


texto = """ 

João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!

"""

print(re.findall(r'j[a-zA-Z]+ão+', texto,flags=re.I))
#print(re.sub(r'jo+ão+','FELIPE',texto,flags=re.I))
print(re.findall(r'jo{1,}ão{1,}', texto,flags=re.I))
print(re.findall(r've{3}m{1,2}', texto,flags=re.I))


texto2 = "João ama ser amado"
print(re.findall(r'ama[do]+', texto2,flags=re.I))#Mostra a palavra com 2 as letras
print(re.findall(r'ama[do]*', texto2,flags=re.I))#Mostra a palavra sem as letras e com 2 as letras
print(re.findall(r'ama[do]{2}', texto2,flags=re.I))#Posso encontrar qualquer uma dessas letras [do]. em 2 buscas.


--------------------------------------""--------------------------------------------------------
#AULA004

# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
#. = qualquer coisa com exceção da quebra de linha

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

#Comportamento guloso: Encontra o máximo de informação passadas.
print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto)) #Eu preciso escapar a barra /. colocando uma barra invertida.

#Comportamento NÃO guloso, ele traz o minimo de informação possivel para minha RegEx, uma por vez.
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))


--------------------------------------""--------------------------------------------------------
#AULA05
# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3

#Grupos: São RegEx colocadas entre parenteses (). 
#Nós acessamos estes GRUPOS por meio dos RETROVISORES \n.
#EXEMPLO ABAIXO

import regex
from pprint import pprint
#Pprint serve para imprimir os resultados um abaixo do outro
#como se fosse \n


texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

#print((re.findall(r'<([dpiv]{1,3})>.+?<\/\1>',texto)))
#tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)',texto)
#pprint(tags)
print("\n")
#for tag in tags:
#  um, dois, tres = tag
#  print(tres)

#cpf = '147.852.953-12'

#print(re.findall(r"((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})",cpf))
#PESQUISAR MAIS SOBRE O COMANDO ?:

#Posso dar nomes aos grupos com ?P<nome> e acessá-los com (?P=nome)
#Exemplo abaixo:

tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>',texto)
pprint(tags)


--------------------------------------""--------------------------------------------------------
#AULA06
# Meta caracteres: 
#^ --> Começa com...
#$ --> Termina com ...
#[^a-z] --> Negação (Neste contexto significa negação) 
#Isso é ótimo para validar(retornar)algo.

cpf = '147.852.953-12'
print(re.findall(r"^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$",cpf))

#Exemplo de [^a-z] --> Negação
print(re.findall(r'[^a-z]+',cpf))

#Exemplo de negação que tira tudo
print(re.findall(r'[^a-z0-9.-]+',cpf))


--------------------------------------""--------------------------------------------------------
from enum import Flag
#AULA07 - INICIAR

# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t] -> Maioria dos Espaços.
# \S -> [^ \r\n\f\n\t]
# \b -> borda 
# \B -> não borda
#
#re.I -> Achar letras maiusculas tambem (IGNORECASE)
#re.A utilizar a tabela ASCII para retonar palavras com acento tbm
#re.M -> Multiline -> -> ^ $
#re.S ->Dotall (tambem le o que vem após a quebra de linha \n)

texto = """ 
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve_Algo 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!

"""
#Pereba que assim as palavras acentuadas ainda não aparecem
print(re.findall(r'[a-zA-Z0-9]+',texto))

#À-ú - Agora as palavras acentuadas aparecem
print(re.findall(r'[a-zA-Z0-9À-ú]+',texto))

#Outram maneira de incluir tudo é utilizando \w+ que pega Underline tbm
print(re.findall(r'\w+',texto))

#A negação do \w é \W
print(re.findall(r'\D+',texto))

#Encontrando palavras que possuem a letra "e" no inicio
print(re.findall(r'\be+\w+',texto))

#Encontrando palavras que possuem a letra "e" no final
print(re.findall(r'\w+e\b',texto))

#Encontrando palavras que possuem 4 letras extamente
print(re.findall(r'\b\w{4}\b',texto, flags = re.I))

cpfs = """
131.768.460-53 ABC
055.123.060-50
955.123.060-90
"""

#Se eu aplicar re.M ele vai retornar os cpfs linha por linha
print(re.findall(r"\d{3}\.\d{3}\.\d{3}\-\d{2}",cpfs,flags=re.M))


--------------------------------------""--------------------------------------------------------
#AULA08
import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Positive lookahead: Encontrou apenas os cpf que tem active com (?=active)
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative lookahead:Encontrou apenas os cpf que NÃO tem active com (?!active)
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive lookahead: 
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind: Vai olhar pra ver se existe a palavra ONLINE para trás com (?<=ONLINE) e retorna a linha que tem ONLINE
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Negative lookbehind: Vai olhar pra ver se existe a palavra ONLINE para trás com (?<=ONLINE) e retorna a linha que NÃO tem ONLINE 
# pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Positive lookbehind
# pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

# Negative lookbehind
# pprint(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

"OBS: POSITIVE LOOKBEHIND E NEGATIVA LOOKBEHIND APENAS CHECAM, MAS NÃO RETORNAM NADA. O QUE RETORNA É A EXPRESSÃO REGULAR!"


--------------------------------------""--------------------------------------------------------
#AULA 09 - INICIAR AINDA
#?: --> Grupo não precisa ser salvo

cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

#result = re.findall(cpf_reg_exp, cpf)
#print(result[0])

#Descobrindo IP valido

#A | quer dizer "ou"
ip_reg_exp = re.compile(r'''
^

(?:
    (?:
  25[0-5]| #Pega qualquer numero de 250 a 255
  2[0-4][0-9]| #200-249
  1[0-9]{2}| #100-199
  [1-9][0-9]| #10-99
  [0-9] #0-9
  )
  \.
){3}
  (?:
    25[0-5]| #Pega qualquer numero de 250 a 255
    2[0-4][0-9]| #200-249
    1[0-9]{2}| #100-199
    [1-9][0-9]| #10-99
    [0-9] #0-9
    )$


''', flags= re.X)  

for i in range(301):
  ip = f'{i}.{i}.{i}.{i}'
  print(ip, ip_reg_exp.findall(ip))   


--------------------------------------""--------------------------------------------------------
#Aula10

# https://regex101.com/r/0OM1oz/1/

import re
from pprint import pprint


regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.MULTILINE
)

test_str = ("698.547.520-54\n"
            "060.235.190-16\n"
            "683.134.960-96\n"
            "899.344.730-62\n"
            "103.778.870-21\n"
            "721.478.580-30\n"
            "366.310.090-14\n"
            "794.289.350-26\n"
            "190.259.410-01\n"
            "000.000.000-01\n"
            "900.000.000-00\n\n"
            "000.000.000-00\n"
            "111.111.111-11\n"
            "222.222.222-22\n"
            "333.333.333-33\n"
            "444.444.444-44\n"
            "555.555.555-55\n"
            "666.666.666-66\n"
            "777.777.777-77\n"
            "888.888.888-88\n"
            "999.999.999-99\n\n"
            )

pprint(regex.findall(test_str))


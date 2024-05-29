"""
Crie um dicionário em Python com os seguintes dados de uma pessoa:
- Nome
- CPF
- RG
- Data de Nascimento
- Gênero
- E-mail
- Telefone
- Tipo sanguíneo
- Profissão
- Empresa

"""

import os

pessoa = {
    "Nome" : input('Nome:'),"CPF"  : input('CPF:'),
    "RG" : input('Digite o seu RG:'),"Data de Nascimento" : input('Data de Nascimento (dd/mm/aaa):'),
    "Gênero" : input('Gênero:'),"E-mail" : input('E-mail:'),
    "Telefone" : input('Telefone:'),"Tipo Sanguíneo" : input('Tipo Sanguíneo:'),
    "Profissão" : input('Profissão:'),"Empresa" : input('Empresa onde trabalha:')
}

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')







"""Paradoxo do Aniversário: Extraído de Birthday Paradox Simulation, by Al Sweigart, al@inventwithpython.com.
Explore the surprising probabilities of the "Birthday Paradox" 
Veja o código em  https://nostarch.com/big-book-small-python-projects

Tags: short, math, simulation"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """ Retorna uma lista de objetos de datas aleatórias para aniversários."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # O ano não é importante para a nossa simulação,
        # desde que todos os aniversários tenha o mesmo ano.
        startOfYear = datetime.date(1970, 1, 1)
        
        # Obtenha um dia aleatório no ano:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    # Retorna o objeto de data de um aniversário que ocorre
    # mais de uma vez na lista de aniversários.
    if len(birthdays) == len(set(birthdays)):
        return None     # Todos os aniversários são únicos, portanto, retorne Nenhum.
    
    # Compare cada aniversário com todos os outros aniversários:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA    # Devolva o aniversário correspondente
            
            
# Mostrando a introdução
print('''O Paradoxo do Aniversário nos mostra que, em um grupo de N pessoas, a probabilidade de duas delas possuirem aniversários
correspondentes é surpreendentemente grande.

Este código realiza uma simulação de Monte Carlo (isto é, simulações aleatórias repetidas) para explorar este conceito.

Desenvolvido por Al Sweigart, contato: al@inventwithpython.com

Digitado para estudo por Jefferson Klamas, contato: jeffersonklamas@gmail.com
''')

print('=' * 120)

# tupla de nomes de meses em ordem:
MONTHS =  ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Continue perguntando até que o usuário insira um valor válido.
    print('Quantos aniversários devo gerar? (MAX 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break    # O usuário inseriu uma valor válido.
print()

# Gerando e exibindo os aniversários.
print(f'Aqui estão {numBDays} aniversários: ')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Exibindo uma vírgula para cada aniversário após o primeiro aniversário.
        print(', ', end='')
    monthName = MONTHS[birthday.month -1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determinando se há dois aniversários correspondentes.
match = getMatch(birthdays)

# Resultaods:
print('Nesta simulação, ', end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print(f"Várias pessoas fazem aniversário em {dateText}.")
else:
    print('Não há datas de nascimento correspondentes.')
print()

# Executando 100,000 simulações:
print(f'Geração de {numBDays} aniversários aleatórios de 100.000 vezes....')
input('Pressione Enter para começar....')

print('\nRodando mais de 100.000 simulações.')
simMatch = 0    # Quantas simulações possuem aniversários correspondentes
for i in range(100_000):
    #
    if i % 10_000 == 0:
        print(i, 'simulações rodando....')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch +1
print('100.000 simulações executadas.\n')

# Exibindo resultados da simulação:
probability = round(simMatch / 100_000 * 100, 2)
print('Resultados simulados: \n')
print(f'De 100,000 simulações entre {numBDays} pessoas, houve um')
print(f'aniversário correspondente nesse grupo {simMatch} vezes. Isso significa')
print(f'que {numBDays} pessoas tem {probability}% de chance de')
print('ter um aniversário em seu grupo.\n')
print('Isso é provavelmente mais do que você imagina!')


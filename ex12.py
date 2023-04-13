votos = {}

while True:
    candidato = input('Digite o nome do candidato (ou fim para cancelar): ')
    if candidato == 'fim':
        break 
    
    #Verifica se o candidato ja recebeu votos antes
    if candidato in votos:
        votos[candidato] += 1
        
    else:
        votos[candidato] = 1
        
print('Resultado da votação: ')
for candidato, quantidade in votos.items():
    print(candidato, '.', quantidade, 'votos')
    
print(votos)
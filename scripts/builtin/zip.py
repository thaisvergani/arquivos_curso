perguntas = ['nome', 'sobrenome', 'altura']
respostas = ['Thaís', 'vergani', '1.60']
for q, a in zip(perguntas, respostas):
    print 'Qual o seu(sua) {0}?  It is {1}.'.format(q, a)

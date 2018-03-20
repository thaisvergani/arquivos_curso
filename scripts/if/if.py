x = int(raw_input("Informe um inteiro: "))

if x < 0:
    x = 0
    print 'Negativo'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Um'
else:
    print 'Mais'

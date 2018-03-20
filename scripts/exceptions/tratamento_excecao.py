while True:
    try:
        x = int(raw_input("informe um numero: "))
        break
    except ValueError:
        print "numero invalido, tente novamente."

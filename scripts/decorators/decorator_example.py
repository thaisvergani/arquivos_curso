def echo_funcname(func):
 
    def finterna(*args, **kwargs):
        print "Chamando funcao: %s()"  % (func.__name__)
        return func(*args, **kwargs)
 
    return finterna
 
def dobro(x):
    """ Uma funcao exemplo qualquer.
    """
    return 2*x
 
dobro_com_print = echo_funcname(dobro)
print dobro_com_print(10)
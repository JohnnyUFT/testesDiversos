def nome_do_objeto(c): #Você sabe dizer qual é o tipo de c?
    try:
        print("Nome do objeto: %s. Id: %d."%(c.__name__, id(c)))
    except:
        print("O objeto " %s " não tem atributo __name__ mas seu id é %d."%(str(c), id(c)))
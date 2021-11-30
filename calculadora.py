def calcule ():
    operacao=input('''
    Insira a operação desejada
    + for soma
    - for subtração
    * for multiplicação
    / for divisão
    ''')

    a = int(input('Escolha seu numero: '))
    b = int(input('Escolha seu numero: '))
    
    if operacao == '+':
        print('{}+{}= ' .format(a,b)) 
        print(a+b)
    elif operacao == '-':
        print('{}-{}= ' .format(a,b)) 
        print(a-b)
    elif operacao == '*':
        print('{}*{}= ' .format(a,b)) 
        print(a*b)
    elif operacao == '/ ':
        if b == 0:
            b = int(input('divisor precisa ser diferente de 0. Insira novamente'))
        print('{}/{}= ' .format(a,b)) 
        print(a/b)
    else:
        print('Digite uma operação valida. inicie novamente.')    

    novamente()

def novamente():
    DNV = input('''
    Se vc deseja calcular novamente
    digite S para SIM e N para NÃO.
    ''')
    if DNV == 'S':
        calcule()
    elif DNV == 'N':
        print('Até mais.')
    else:
        DNV()

    calcule()


calcule()

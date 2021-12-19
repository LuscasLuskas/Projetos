from time import sleep
def calcule ():
    operacao=input('''
    Insira a operação desejada:

    pl para indice de Laspeyres

    pp para indice de Paasche

    ps para indice de Preço imples

    ''')
    if operacao == 'ps':
        A = float(input('Preços para o ano i(Pi): '))
        B = float(input('Preços para o ano base(Pbase): '))
        print('{}/{}= ' .format(A,B))
        print((A/B)*100)
        novamente()

    elif operacao == 'pp' or 'pl':
        a = float(input('Preço no periodo considerado(Pt): '))
        b = float(input('Quantidade no periodo-base(Q0): '))
        c = float(input('Preço no periodo-base(P0): '))
        d = float(input('Quantidade no periodo considerado(Qt): '))

        if operacao == 'pl':
            print('{}*{}/{}*{}=' .format(a,b,c,d)) 
            print((a*b)/(c*b)*100)
            novamente()
        elif operacao == 'pp':
            print('{}*{}/{}*{}=' .format(a,b,c,d)) 
            print((a*d)/(c*d)*100)
            novamente()
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
        sleep(2)
    else:
        DNV()

calcule()

    

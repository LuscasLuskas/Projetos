from time import sleep
def calcule():
    media=input('''
    Aperte "Enter" 
    para calcular a
    media de um aluno''')

    a = float(input('insira a primeira nota: '))
    b = float(input('insira a segunda nota: '))
    c = float(input('insira a terceira nota: '))

    
    print(f'A Media é: {(a+b+c)/3}')

    novamente()

def novamente():
    Dnv = input('''
    Se vc deseja 
    calcular novamente
    digite S para SIM e
     N para NÃO:  ''')
    if Dnv == 'S':
        calcule()
    elif Dnv == 'N':
        print('Ate mais.') 
        sleep(2)
    else:
        Dnv   

calcule()




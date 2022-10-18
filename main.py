def pot_recursiva(num1, num2):
    if (num2 == 0 or num2 == 1):
        return num1
    else:
        return (num1 * pot_recursiva(num1, num2 - 1))


def validacion(num):
    while not (num.isnumeric()):
        print('Ingrese valido')
        num = (input("ingrese el numero\n"))
    else:
        return int(num)


calc = True
while calc == True:
    num1 = validacion(input('Ingrese primer numero '))
    num2 = validacion(input('Ingrese segundo numero '))
    operador = input('Ingrese el operador:(+,-,*,/,**,***) ')
    while operador not in ('+', '-', '*', '/', '**', '***'):
        print('Ingresa un operador válido')
        operador = input('Ingrese el operador: ')

    if (operador == '+'):
        resultado = num1 + num2
    elif (operador == '-'):
        resultado = num1 - num2
    elif (operador == '*'):
        resultado = num1 * num2
    elif (operador == '/'):
        resultado = num1 // num2
    elif (operador == '**'):
        resultado = (num1 ** num2)
    elif (operador == '***'):
        resultado = pot_recursiva(num1, num2)

    print('el resultado es: ', resultado)
    rpt = input('Si desea continuar presione "si", caso contrario, presiona cualquier tecla ').upper()
    if rpt != 'SI':
        calc = False
# converte binario em decimal
def binaryToDecimal(n):
    return int(n, 2)


if __name__ == '__main__':
    contem = False
# verificar se o valor do texto é maior de 8 e não contem valores diferentes de 0 e 1
    print()
    valor = input('Informe um Valor Binario: ')
    print()
    if len(valor) <= 8:
        for teste in valor:
            if (teste != '0') and (teste != '1'):
                contem = True

        if contem:
            print('Apenas valores 0 e 1')
            print()
        else:
            print(f'Decimal do numero é {binaryToDecimal(valor)}')
            print()
    else:
        print(f'Só é permitido até 8 digitos, você digitou {len(valor)}')
        print()

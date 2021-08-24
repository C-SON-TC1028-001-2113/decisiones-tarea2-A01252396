def main():
    #escribe tu código abajo de esta línea
    l1 = int(input("Ingresa la medida del lado 1: "))
    l2 = int(input("Ingresa la medida del lado 2: "))
    l3 = int(input("Ingresa la medida del lado 3: "))

    if l1 > 0 and l2 > 0 and l3 > 0:
        if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
            if l1 == l2 and l1 == l3:
                print('ES UN TRIANGULO EQUILATERO')
            elif l1 == l2 or l1 == l3 or l2 == l3:
                print('ES UN TRIANGULO ISOSCELES')
            else:
                print('ES UN TRIANGULO ESCALENO')
        else: 
            print('NO ES TRIANGULO')
    else:
        print('NO ES TRIANGULO')
    


if __name__=='__main__':
    main()

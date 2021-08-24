def main():
    #escribe tu código abajo de esta línea
    edad = int(input('Ingresa tu edad: '))
    mayor = edad >= 18
    menor = edad > 0

    if mayor and menor:
        identi = str(input('¿Tienes identificación oficial? (s/n): '))
        if identi == 's' :
            print ('Trámite de licencia concedido')
        elif identi == 'n':
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')
    if not mayor and menor :
        print('No cumples requisitos')
    if not mayor and not menor :
        print('Respuesta incorrecta')



if __name__=='__main__':
    main()


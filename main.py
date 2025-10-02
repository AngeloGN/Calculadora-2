import math
salir=""
while salir.lower() !="salir":

        print("bienvenido a la calculadora")
        print("escoge una opción")
        print("1.sumar")
        print("2.restar")
        print("3.dividir")
        print("4.multiplicar")
        print("5.potencia al cuadrado")
        print("6.raiz cuadrada")
        print("escribe (Salir)para acabar el programa")

        opcion= input("escoge una de las opciones ")


        if opcion.lower()=="salir":
             salir="salir"
        elif opcion not in ("1","2","3","4","5","6"):
            print("esta opcion no es valida")
        else:
            opcion=int(opcion)

        match opcion:
            case 1:
                num1=float(input("dame el primer numero a operar "))
                num2=float(input("dame el segundo numero a operar "))
                resultado=num1+num2
                print("el resultado es: ",resultado)

            case 2:
                num1=float(input("dame el primer numero a operar "))
                num2=float(input("dame el segundo numero a operar "))
                resultado=num1-num2
                print("el resultado es: ",resultado)
        
            case 3:
                num1=float(input("dame el primer numero a operar "))
                num2=float(input("dame el segundo numero a operar "))
                resultado=num1/num2
                print("el resultado es:",resultado)
        
            case 4:
                num1=float(input("dame el primer numero a operar "))
                num2=float(input("dame el segundo numero a operar "))
                resultado=num1*num2
                print("el resultado es: ",resultado)

            case 5:
                num=float(input("dame el numero a elevar al cuadrado"))
                resultado= num**2
                print("el resultado es: ",resultado)

            case 6:
                num=float(input("dame el numero para obtener su raiz cuadrada"))
                if num<0:
                    print("error no puedo sacar raiz cuadrada de numero negativos")
                else:
                    resultado= math.sqrt(num)
                print("la raiz cuadrada es: ",resultado )
        
        

    


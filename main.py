print("bienvenido a la calculadora")
print("escoge una opción")
print("1.sumar")
print("2.restar")
print("3.dividir")
print("4.multiplicar")

opcion=int(input("escoge una de las opciones "))

num1=float(input("dame el primer numero a operar "))
num2=float(input("dame el segundo numero a operar "))

if opcion>=4:
    print("esta opcion es invalida")


match opcion:
    case 1:
        resultado=num1+num2
        print("el resultado es: ",resultado)

    case 2:
        resultado=num1-num2
        print("el resultado es: ",resultado)
    
    case 3:
        resultado=num1/num2
        print("el resultado es:",resultado)
    
    case 4:
        resultado=num1*num2
        print("el resultado es: ",resultado)


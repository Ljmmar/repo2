def calcular_imc(peso, altura):
    """
    Función para calcular el índice de masa corporal (IMC).
    """
    return peso / (altura ** 2) 

def clasificar_imc(imc):
    """
    Función para clasificar el IMC en categorías.
    """
    if imc < 18.5:
        return "Delgado"
    elif 18.5 <= imc < 25:
        return "Peso apropiado"
    else:
        return "Sobrepeso"

def main():
    """
    Función principal que solicita los datos al usuario y muestra el resultado.
    """
    nombre = input("Ingrese su nombre: ")
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kilogramos: "))
    edad = int(input("Ingrese su edad en años: "))

    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)

    print("\nResultado para", nombre)
    print("----------------------------")
    print("Edad:", edad, "años")
    print("Altura:", altura, "metros")
    print("Peso:", peso, "kilogramos")
    print("IMC:", round(imc, 2))
    print("Clasificación de IMC:", clasificacion)

if __name__ == "__main__":
    main()
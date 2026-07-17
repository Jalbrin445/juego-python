# Importación de módulos a utilizar

import random # Módulo utilizado para obtener valores en aleatorio
import string # Este modulo contienen constantes predefinidas como digitos, listas del alfabeto o signos de puntuación


# Sección de clase para el manejo de errores o excepciones
class LongitudInvalidaErrorJAMG(Exception):
    """
    Docstring: Esta excepción será lanzada o llamada cuando
    la longitud de la contraseña sea menor a 8 caracteres
    """
    def __init__(self, mensajeJAMG="La longitud de la contraseña debe ser mayor o igual a los 8 carácteres"):
        self.mensajeJAMG = mensajeJAMG
        super().__init__(self.mensajeJAMG)

class DatosNoNumericosErrorJAMG(Exception):
    """
    Docstring: Esta excepción será lanzada cuando la entrada 
    del usuario no es un número entero.
    """

    def __init__(self, mensajeJAMG="Error: debe ingresar un valor de tipo numérico entero (int)"):
        self.mensajeJAMG = mensajeJAMG
        super().__init__(self.mensajeJAMG)

class ContrasenaIncorrectaErrorJAMG(Exception):
    """
    Docstring: clase para cuando la contraseña sea incorrecta, es decir, no cumpla con
    lo requerido
    """
    def __init__(self, mensajeJAMG="La contraseña generada es inválida y no cumple con los requisitos estrictos"):
        self.mensajeJAMG = mensajeJAMG
        super().__init__(self.mensajeJAMG)

## Sección de clases principales

# Clase Cofre

class CofreJAMG:

    """
    Docstring: clase encargada para definir los tipos de cofres 
    según la contraseña y la aletoriedad:
    """
    TIPOS_COFRE_POSITIVO_JAMG = {
        "Común": 10,
        "Raro": 25,
        "Legendario": 50
    }
    def __init__(self, es_validoJAMG=True):

        if es_validoJAMG:

            self.tipoJAMG = random.choice(list(self.TIPOS_COFRE_POSITIVO_JAMG.keys())) # Se selecciona el cofre de forma aleatoria, seleccionando solo las llaves, es decir, común, raro y legendario
            self.puntosJAMG = self.TIPOS_COFRE_POSITIVO_JAMG[self.tipoJAMG] # aquí se selecciona la cantidad de puntos según el cofre escogido anteriormente
        else:
            # Si no hay uno valido entonces se define como del tipo siguiente:
            self.tipoJAMG = "Maldito"
            self.puntosJAMG = -20
        
    def obtener_detallesJAMG(self):

        """
        Método utilizado para obtener los datos detallados
        del cofre seleccionado
        """
        return self.tipoJAMG, self.puntosJAMG

# Clase contraseña
class ContrasenaJAMG:

    """
    Docstring: esta clase esta diseñada para crear y validar 
    las constraseñas según los criterios de evaluación
    """

    CARACTERES_ESPECIALES_JAMG = "¿¡?=)(/¨*+-%&$#!." # String de caracteres especiales
    
    def __init__(self, longitudJAMG):
        
        self.longitudJAMG = longitudJAMG # este atributo es para que el usuario pueda ingresar la longitud por linea de comandos
        self.valor = ""
    
    def validar_requisitosJAMG(self, passwordJAMG):
        """
        Método utilizado para validar que los requisitos 
        de la contraseña creada si se cumplan según los criterios
        de aceptación
        """
        tiene_mayusculaJAMG = any(c.isupper() for c in passwordJAMG) # any devuelve True si por lo menos uno de los valores es una mayuscula según el método .isupper()
        tiene_minusculaJAMG = any(c.islower() for c in passwordJAMG)
        tiene_numeroJAMG = any(c.isdigit() for c in passwordJAMG)
        tiene_caracter_especialJAMG = any(c in self.CARACTERES_ESPECIALES_JAMG for c in passwordJAMG)
        sin_repetidosJAMG = len(passwordJAMG) == len(set(passwordJAMG))

        return tiene_mayusculaJAMG and tiene_minusculaJAMG and tiene_numeroJAMG and tiene_caracter_especialJAMG and sin_repetidosJAMG # devuelve un valor True o False
    
    def generar_contrasenaJAMG(self):
        """
        Este es el método utilizado para generar las contraseñas de forma
        completamente aleatoria, teniendo en cuenta que debe pasar la validación
        estricta, es decir, el método validar_requisitoJAMG
        """

        todos_los_caracteresJAMG = string.ascii_letters + string.digits + self.CARACTERES_ESPECIALES_JAMG

        #Luego se convierte los caracteres anteriores a una lista para evaluar de forma más sencilla todo

        lista_disponible = list(set(todos_los_caracteresJAMG))

        if self.longitudJAMG > len(lista_disponible):
            # Esto es para añadir más restricción o validación estricta, ya que no tiene sentido que la longitud de la contraseña sea mayor a la cantidad total de caracteres disponibles
            raise LongitudInvalidaErrorJAMG("Longitud excesiva para generar caracteres sin repetir")
        
        caracteres_elegidosJAMG = random.sample(lista_disponible, self.longitudJAMG) # Con este método se pueden generar las contraseñas a partir de una lista de valores y una longitud, dando como resultado una contraseña sin caracteres repetidos
        self.valor ="".join(caracteres_elegidosJAMG)

        if not self.validar_requisitosJAMG(self.valor):
            # Esta es la validación estricta obligatoria
            raise ContrasenaIncorrectaErrorJAMG 
        
        return self.valor
# clase Juego Cazador

class JuegoCazadorJAMG:

    """
    Docstring: esta es la clase principal, la cual contiene toda
    la lógica de ejecución del juego
    """

    def __init__(self):
        self.puntaje_totalJAMG = 0

    
    def juego(self):
        """
        Método utilizado para gestionar la lǵoica de una ronda del juego.
        Solicita la longitud, genera la contraseña, determina el cofre, 
        actualiza el puntaje y muestra los resultados
        """

        print("\n" + "-"*40)
        print(f"Puntaje actual: {self.puntaje_totalJAMG} puntos")
        print("-"*50)

        while True:
            try:
                entrada_longitudJAMG = input("Ingresa la longitud de la contraseña: ")
                
                if not entrada_longitudJAMG.isdigit():
                    raise DatosNoNumericosErrorJAMG()
                
                longitud_usuario = int(entrada_longitudJAMG)
                if longitud_usuario < 8:
                    raise LongitudInvalidaErrorJAMG()
                break

            except DatosNoNumericosErrorJAMG as e:
                print(f"Error: {e}")

            except LongitudInvalidaErrorJAMG as e:
                print(f"Error: {e}")
            
            except Exception as e:
                print(f"Ha ocurrido un error inesperado: {e}")
        
        es_contrasena_validaJAMG = False
        contrasena_objJAMG = ContrasenaJAMG(longitud_usuario)
        try:

            contrasena_generadaJAMG = contrasena_objJAMG.generar_contrasenaJAMG()

            es_contrasena_validaJAMG = True
        except ContrasenaIncorrectaErrorJAMG as e:
            print(f"Error: {e}")
            contrasena_generadaJAMG = "[Contraseña inválida]"
        
        except Exception as e:
            print(f"Ha ocurrido un error durante la generación: {e}")
            contrasena_generadaJAMG = "[Error en la generación de contraseña]"

            return
        
        cofreJAMG = CofreJAMG(es_contrasena_validaJAMG)
        tipo_cofreJAMG, puntos_cofreJAMG = cofreJAMG.obtener_detallesJAMG()

        self.puntaje_totalJAMG += puntos_cofreJAMG

        print("\n" + "="*40)
        print("Resultados de la ronda")
        print("="*50)
        print(f"Contraseña generada: {contrasena_generadaJAMG}")
        print(f"Tipo de cofre: {tipo_cofreJAMG}")
        print(f"Puntos otorgados: {puntos_cofreJAMG}")
        print(f"Puntaje acumulado: {self.puntaje_totalJAMG}")
        print("="*50)
    
    def mostrar_resumen_finalJAMG(self):
        """
        Método utilizado para mostrar el resumen final del juego
        """
        print("Resumen final")
        print(f"Puntaje total obtenido en tu aventura: {self.puntaje_totalJAMG}")
        

    def iniciar(self):
        """
        Método para iniciar el juego
        """

        print("\n" + "="*40)
        print("Bienvenido, cazador de contraseñas")
        print("="*50)
        print("Recuerda que las contraseñas deben ser seguras y cumplir con")
        print("todos los requisitos para evitar un cofre maldito\n")
        # Este bucle es para controlar la ejecución del juego
        jugando = True # Variable de control
        while jugando:

            self.juego()
            while True:
                # Este bucle es para comprobar si el usuario quiere seguir jugando o no y si es así entonces seguir ejecutando el bucle externo que contiene el método juego
                try:
                    
                    continuar = input("\n ¿Quieres seguir jugando? (s/n): ").strip().lower()
                    # Estructura condicional para comprobar si el usuario quiere seguir jugando o no
                    if continuar in ('s', 'si', 'sí'):
                        break
                    elif continuar in ('n', 'no'):
                        jugando = False
                        break
                    else:
                        print("Por favor, ingresa 's' (para sí) o 'n' (para no)")              

                except Exception:
                    # manejo de excepción por si ocurre un error inesperado en la entrada
                    print("Ha ocurrido un error inesperado. Intenta de nuevo")
        
        self.mostrar_resumen_finalJAMG() # Método utilizado cuando se finaliza el juego
        print("Graicas por jugar, hasta la próximaAA")

    
# Punto de entrada del programa para ejecutarlo directamente
if __name__ == "__main__":


    juego_cazador = JuegoCazadorJAMG()
    juego_cazador.iniciar()
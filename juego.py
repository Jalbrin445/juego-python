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
        
    def obtener_detalles(self):

        """
        Método utilizado para obtener los datos detallados
        del cofre seleccionado
        """
        return self.tipo, self.puntos

# Clase contraseña
class ContrasenaJAMG:

    """
    Docstring: esta clase esta diseñada para crear y validar 
    las constraseñas según los criterios de evaluación
    """
    def __init__(self):
        pass

# clase Juego Cazador

class JuegoCazadorJAMG:

    """
    Docstring: esta es la clase principal, la cual contiene toda
    la lógica de ejecución del juego
    """

    def __init__(self):
        pass


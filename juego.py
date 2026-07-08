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


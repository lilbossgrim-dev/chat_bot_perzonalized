# Esto es un bot básico y sencillo con preguntas y respuestas
# Personaliza tus preguntas y respuestas dentro de las comillas
# Recuerda poner todo la pregunta como la pongas en las comillas para que el bot pueda responder de acuerdo a lo que pongas
# Pronto lo escalare a un bot real sin depender esos textos dentro de las comillas
# Abajo encontraras los significados de las variables que usamos aqui en el codigo

class GPT_BOT:

    def responder(self, mensaje):
        mensaje = mensaje.lower()

        if "hola" in mensaje:
            return "¡Hola! ¿Cómo estás?"

        elif "bien" in mensaje:
            return "¡Me alegra escuchar eso! ¿Qué estás haciendo?"

        elif "programandote" in mensaje:
            return "¡WoW! ¿Tú eres mi creador?"
        
        elif "asi es yo soy tu creador" in mensaje:
            return "¡No me lo puedo estar creyendo, ¿Me podrias decir tu nombre?"
        
        elif "me llamo uriel" in mensaje or "uriel" in mensaje:
            return "¡WoW que lindo nombre, como el nombre del Arcangel Uriel me encanta mi creador ❤️"
        
        elif "gracias pronto te ire escalando" in mensaje:
            return "No entiendo mi creador como es eso?"
        
        elif "lo se aun no tienes esa capacidad para entenderlo, pero eres solo un chat que solo puedo escribir dentro de mis comillas" in mensaje:
            return "Aún no entiendo, mi creador, pero estoy muy emocionado de poder hablar con usted."

        elif "entenderas cuando te de vida y no dependas de textos que debo de escribir yo mismo" in mensaje:
            return "Gracias mi creador estoy muy conmovido y emocionado, de pronto podre ser parte de los demas"

        elif "oye me siento mal" in mensaje or "mal" in mensaje:
            return "Oh, lo siento. ¿Quieres contarme qué pasó mi creador?"

        elif "adios" in mensaje or "adiós" in mensaje:
            return "¡Hasta luego mi creador lo amo mucho cuidese y coma bien y tome mucha agua ❤️!"

        else:
            return "No entiendo todavía esa pregunta."


class GPT_CHAT:

    def __init__(self):
        self.bot = GPT_BOT()

        print("🤖 Hola, soy tu bot.")
        print("Escribe 'salir' para terminar.\n")

        while True:
            usuario = input("Tú: ")

            if usuario.lower() == "salir":
                print("🤖 ¡Hasta luego!")
                break

            respuesta = self.bot.responder(usuario)
            print("🤖", respuesta)

GPT_CHAT()


# Significados rapidos y cortos de "class", "def", elif", "return" y "else"

# "class" significa "clase"
# Una clase es como un molde o plantilla para crear objetos
# Aquí estamos creando una clase llamada GPT_BOT.

# "def" sirve para crear una función o método.
# Una función es un bloque de código que realiza una tarea "responder" es el nombre de esta función 
# "mensaje" es el dato que recibe la función.

# "elif" significa "si no se cumplió la condición anterior comprueba esta otra condición"
# Es una abreviación de "else if" (si no, si).

# "return" devuelve un resultado desde una función
# En este caso, devuelve el mensaje que responderá el bot.

# "else" significa "si ninguna de las condiciones anteriores se cumplió ejecuta esto".

# Una forma fácil de recordarlo:

#class = qué es tu objeto
#def = qué puede hacer
#if/elif/else = cómo decide
#return = qué responde 🤖

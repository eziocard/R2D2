categories = [
    "ABRIR_PROYECTO",
    "CREAR_PROYECTO",
    "SALUDO",
    "DESCONOCIDO"
]

train_dataset = [
    # ABRIR
    ("abre el proyecto chatbot", 0),
    ("abre chatbot", 0),
    ("quiero abrir dashboard", 0),
    ("abre dashboard", 0),
    ("necesito el proyecto inventario", 0),
    ("trabajar en web_tienda", 0),
    ("abre mi proyecto landing", 0),
    ("quiero entrar al proyecto bot", 0),

    # CREAR
    ("crea un proyecto llamado scraper en python", 1),
    ("creame un proyecto en react llamado landing", 1),
    ("crea landing en react", 1),
    ("haz un proyecto en python llamado bot", 1),
    ("necesito un proyecto nuevo en react", 1),
    ("genera un proyecto llamado api en python", 1),
    ("quiero crear un proyecto de react llamado dashboard", 1),
    ("crea una aplicación llamada tienda en react", 1),

    # =====================
    # SALUDOS
    # =====================
    ("hola", 2),
    ("hola r2d2", 2),
    ("buenas", 2),
    ("buenos dias", 2),
    ("buenas tardes", 2),
    ("como estas", 2),
    ("que tal", 2),
    ("hola amigo", 2),
    ("saludos", 2),

    # DESCONOCIDO
    ("que hora es", 3),
    ("quiero comer pizza", 3),
    ("dime un chiste", 3),
    ("cuentame algo", 3),
]

answers = {
    "ABRIR_PROYECTO": "Buscando el proyecto...",
    "CREAR_PROYECTO": "Creando el proyecto...",
    "SALUDO":
        (
            "Hola, soy R2D2.\n"
            "Puedo ayudarte a crear y abrir "
            "proyectos de desarrollo."
        ),
    "DESCONOCIDO":
        "No entendí la solicitud."
}

actions = {
    "ABRIR_PROYECTO": None,
    "CREAR_PROYECTO": None,
    "SALUDO":
        (
            "Hola, soy R2D2.\n"
            "Puedo ayudarte a crear y abrir "
            "proyectos de desarrollo."
        ),
}
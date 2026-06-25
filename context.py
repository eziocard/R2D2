categories = [
    "ABRIR_PROYECTO",
    "CREAR_PROYECTO",
    "SALUDO",
    "DESCONOCIDO",
    "LISTAR_PROYECTOS",
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
    ("¿como estas?",2),
    ("como estas?", 2),
    ("que tal", 2),
    ("hola amigo", 2),
    ("saludos", 2),

    # DESCONOCIDO
    ("que hora es", 3),
    ("quiero comer pizza", 3),
    ("dime un chiste", 3),
    ("cuentame algo", 3),

        # LISTAR PROYECTOS
    ("muestrame los proyectos", 4),
    ("que proyectos tengo", 4),
    ("lista mis proyectos", 4),
    ("listar proyectos",4),
    ("ver proyectos",4),
    ("muestra mis proyectos", 4),
    ("dime que proyectos hay", 4),
    ("ver mis proyectos", 4),
    ("cuales son mis proyectos", 4),

]

answers = {
    "ABRIR_PROYECTO": "Buscando el proyecto...",
    "CREAR_PROYECTO": "Creando el proyecto...",
    "SALUDO": {
        "default": [
            "Hola, soy R2D2. ¿En qué proyecto trabajamos hoy?",
            "¡Buenas! Listo para abrir o crear proyectos.",
            "Hey, aquí R2D2. ¿Abrimos algo?",
        ],
        "como estas": "Funcionando al 100%. ¿Abrimos un proyecto?",
        "como estas?": "Funcionando al 100%. ¿Abrimos un proyecto?",
        "¿como estas?": "Funcionando al 100%. ¿Abrimos un proyecto?",
        "que tal":    "Todo en orden. ¿En qué te ayudo?",
        "buenos dias": "¡Buenos días! ¿Arrancamos con algún proyecto?",
        "buenas tardes": "¡Buenas tardes! ¿Qué construimos hoy?",
    },
    "DESCONOCIDO": "No entendí la solicitud.",
    "LISTAR_PROYECTOS": "Revisando tu carpeta de proyectos...",
}


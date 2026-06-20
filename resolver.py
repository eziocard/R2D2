import re
import subprocess
from pathlib import Path


PROYECTOS_DIR = Path.home() / "Documents" / "Proyectos"


TECNOLOGIAS = {
    "react": "react",
    "python": "python",
}



# EXTRACCIÓN (regex sobre la frase original, no sobre la categoría)

def extraer_nombre_abrir(texto):
    """Busca el nombre del proyecto después de la palabra 'proyecto'."""
    match = re.search(r"proyecto\s+([a-zA-Z0-9_\-]+)", texto, re.IGNORECASE)
    return match.group(1) if match else None


def extraer_datos_crear(texto):
    texto = texto.lower()

    tecnologia = None
    for tech in TECNOLOGIAS:
        if tech in texto:
            tecnologia = tech
            break

    patrones = [
        r"llamado\s+([a-zA-Z0-9_\-]+)",
        r"proyecto\s+([a-zA-Z0-9_\-]+)",
        r"crea\s+(?:el\s+)?proyecto\s+([a-zA-Z0-9_\-]+)",
        r"crear\s+(?:el\s+)?proyecto\s+([a-zA-Z0-9_\-]+)",
    ]

    nombre = None

    for patron in patrones:
        match = re.search(patron, texto, re.IGNORECASE)
        if match:
            candidato = match.group(1)

            if candidato not in TECNOLOGIAS:
                nombre = candidato
                break

    return nombre, tecnologia


# ABRIR PROYECTO

def abrir_proyecto(nombre):
    if nombre is None:
        print(" [PROYECTOS]: No identifiqué el nombre. Intenta: 'abre el proyecto <nombre>'.")
        return

    ruta = PROYECTOS_DIR / nombre
    if not ruta.exists():
        print(f" [PROYECTOS]: No encontré '{nombre}' en {PROYECTOS_DIR}.")
        return

    try:
        subprocess.Popen(["code", str(ruta)])
        print(f" [PROYECTOS]: Abriendo '{nombre}' en VS Code...")
    except FileNotFoundError:
        print(" [PROYECTOS]: No encontré el comando 'code'. Verifica que VS Code esté instalado y en el PATH (prueba 'code --version' en una terminal).")


# CREAR PROYECTO

def crear_proyecto_react(ruta):
    print(f" [PROYECTOS]: Generando proyecto React (Vite) en '{ruta.name}'...")
    try:
        resultado = subprocess.run(
            ["pnpm", "create", "vite@latest", ruta.name, "--", "--template", "react"],
            cwd=PROYECTOS_DIR,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        print(" [PROYECTOS]: No encontré 'npm'. ¿Está Node.js instalado?")
        return

    if resultado.returncode != 0:
        print(f" [PROYECTOS]: Error al crear el proyecto: {resultado.stderr.strip()}")
        return

    print(f" [PROYECTOS]: Proyecto creado. Próximos pasos:\n   cd {ruta}\n   npm install\n   npm run dev")


def crear_proyecto_python(ruta):
    print(f" [PROYECTOS]: Generando proyecto Python en '{ruta.name}'...")
    ruta.mkdir(parents=True)
    (ruta / "main.py").write_text(f"print('Hola desde {ruta.name}')\n")
    (ruta / "requirements.txt").write_text("")
    (ruta / "README.md").write_text(f"# {ruta.name}\n")
    print(f" [PROYECTOS]: Proyecto creado en {ruta}.")


def crear_proyecto(nombre, tecnologia):
    if nombre is None:
        print(" [PROYECTOS]: No identifiqué el nombre. Intenta: 'crea un proyecto llamado <nombre> en react/python'.")
        return

    if tecnologia is None:
        print(" [PROYECTOS]: No identifiqué la tecnología (react/python). Inclúyela en la frase.")
        return

    PROYECTOS_DIR.mkdir(parents=True, exist_ok=True)
    ruta = PROYECTOS_DIR / nombre

    if ruta.exists():
        print(f" [PROYECTOS]: Ya existe un proyecto llamado '{nombre}'. Elige otro nombre.")
        return

    if tecnologia == "react":
        crear_proyecto_react(ruta)
    elif tecnologia == "python":
        crear_proyecto_python(ruta)


def listar_proyectos():
    if not PROYECTOS_DIR.exists():
        print(f" [PROYECTOS]: La carpeta {PROYECTOS_DIR} todavía no existe.")
        return
 
    proyectos = sorted(p.name for p in PROYECTOS_DIR.iterdir() if p.is_dir())
 
    if not proyectos:
        print(f" [PROYECTOS]: No hay proyectos todavía en {PROYECTOS_DIR}.")
        return
 
    print(f" [PROYECTOS]: Tienes {len(proyectos)} proyecto(s) en {PROYECTOS_DIR}:")
    for nombre in proyectos:
        print(f"   - {nombre}")
 


# ==============================================================================
# PUNTO DE ENTRADA ÚNICO (lo llama infer() desde functions.py)
# ==============================================================================
def manejar_proyecto(categoria, frase_original):
    if categoria == "ABRIR_PROYECTO":
        nombre = extraer_nombre_abrir(frase_original)
        abrir_proyecto(nombre)
    elif categoria == "CREAR_PROYECTO":
        nombre, tecnologia = extraer_datos_crear(frase_original)
        crear_proyecto(nombre, tecnologia)

    elif categoria == "LISTAR_PROYECTOS":
        listar_proyectos()

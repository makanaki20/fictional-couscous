import os
import random
import string
import time

BASE = os.path.join(os.getcwd(), "resultados")
os.makedirs(BASE, exist_ok=True)

LONGITUD_PASSWORD = 8
FORMATO = "{user}:{password}"

def banner():
    os.system("clear")

    VERDE = "\033[92m"
    CYAN = "\033[96m"
    ROJO = "\033[91m"
    RESET = "\033[0m"

    print(f"""{VERDE}

███╗   ███╗ █████╗ ██╗  ██╗ █████╗
████╗ ████║██╔══██╗██║ ██╔╝██╔══██╗
██╔████╔██║███████║█████╔╝ ███████║
██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══██║
██║ ╚═╝ ██║██║  ██║██║  ██╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

{CYAN}
╔══════════════════════════════════════╗
║      MAKANAKI COMBO GENERATOR       ║
║           VERSION 3.0 PRO           ║
╚══════════════════════════════════════╝
{RESET}
""")

def generar_password(longitud):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(longitud))

def crear_desde_lista():

    banner()

    archivo = input("Ruta lista nombres: ").strip()

    if not os.path.exists(archivo):
        print("\nArchivo no encontrado")
        input("\nENTER para continuar...")
        return

    salida = os.path.join(BASE, "usuarios_generados.txt")

    with open(archivo, "r", encoding="utf-8") as f:
        nombres = [x.strip() for x in f if x.strip()]

    with open(salida, "w", encoding="utf-8") as out:

        for nombre in nombres:

            password = generar_password(LONGITUD_PASSWORD)

            linea = FORMATO.format(
                user=nombre,
                password=password
            )

            out.write(linea + "\n")

    print("\n" + "=" * 50)
    print("GENERACION COMPLETADA")
    print("Total:", len(nombres))
    print("Archivo:", salida)
    print("=" * 50)

    input("Presiona ENTER para volver al menu...")

def eliminar_duplicados():

    banner()

    ruta = input("Archivo: ").strip()

    if not os.path.exists(ruta):
        print("Archivo no encontrado")
        input("ENTER...")
        return

    salida = os.path.join(BASE, "sin_duplicados.txt")

    vistos = set()

    with open(ruta, "r", encoding="utf-8") as f:
        with open(salida, "w", encoding="utf-8") as out:

            for linea in f:

                linea = linea.strip()

                if linea and linea not in vistos:
                    vistos.add(linea)
                    out.write(linea + "\n")

    print("\nGuardado:")
    print(salida)

    input("\nENTER para continuar...")

def configurar_longitud():

    global LONGITUD_PASSWORD

    banner()

    try:
        LONGITUD_PASSWORD = int(input("Longitud password: "))
        print("Guardado")
    except:
        print("Valor invalido")

    input("\nENTER...")

def configurar_formato():

    global FORMATO

    banner()

    print("""
1 usuario:password
2 usuario|password
3 usuario,password
4 usuario-password
""")

    op = input(">> ")

    if op == "1":
        FORMATO = "{user}:{password}"

    elif op == "2":
        FORMATO = "{user}|{password}"

    elif op == "3":
        FORMATO = "{user},{password}"

    elif op == "4":
        FORMATO = "{user}-{password}"

    print("Formato guardado")
    input("\nENTER...")

def menu():

    while True:

        banner()

        print("""
1 Crear combo con lista de nombres
2 Eliminar duplicados
3 Configurar longitud password
4 Configurar formato
0 Salir
""")

        op = input(">> ").strip()

        if op == "1":
            crear_desde_lista()

        elif op == "2":
            eliminar_duplicados()

        elif op == "3":
            configurar_longitud()

        elif op == "4":
            configurar_formato()

        elif op == "0":
            print("\nSaliendo...")
            time.sleep(1)
            break

        else:
            print("Opcion invalida")
            time.sleep(1)

if __name__ == "__main__":
    menu()

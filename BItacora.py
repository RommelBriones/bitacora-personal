import os
from datetime import datetime

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_FOLDER, "bitacora.txt")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("BITÁCORA PERSONAL")
    print("=" * 40)
    print("1. Agregar entrada a la bitácora")
    print("2. Ver todas las entradas")
    print("3. Buscar entrada por palabra clave")
    print("4. Salir")
    print("=" * 40)


def show_header(header_text):
    print(header_text)
    print("=" * 40 + "\n")


def validate_menu_option(option, first_option, last_option):
    option_number = int(option)
    if first_option <= option_number <= last_option:
        return option_number
    return None


def read_menu_option(first_option: int, last_option: int):
    option = input("Escriba el número de su opción> ").strip()

    if not option:
        print("No ha introducido ningún número.")
        return None

    try:
        option_number = validate_menu_option(option, first_option, last_option)
        if option_number is not None:
            return option_number
        else:
            print("Escriba un número de opción válido del menú.")
            return None
    except ValueError:
        print("La entrada no es un número de opción válido.")
        return None


def read_multiline_entry():
    print("Escribe tu entrada (Escribe 'FIN' en una línea nueva para terminar):\n")
    entry_lines = []
    while True:
        line = input("> ")
        if line.strip().upper() == "FIN":
            break
        entry_lines.append(line)
    entry_lines.insert(0, datetime.now().strftime("%d-%m-%Y %H:%M"))
    return "\n".join(entry_lines) + "\n===FIN DE REGISTRO===\n"


def get_file_records():
    file_content = read_file(FILE_PATH)
    if file_content:
        records = file_content.split("\n===FIN DE REGISTRO===\n")
        records = [r.strip() for r in records if r.strip()]
        return records
    else:
        return []


# ------------------------------------------------------------
# ---- FILE HANDLING FUNCTIONS -------
def read_file(filename):
    if not os.path.exists(filename):
        return ""
    if os.path.getsize(filename) == 0:
        return ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except Exception as e:
        print(f"\nERROR al leer los datos: {e}")
        return ""


def save_file(file_content, filename):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(file_content)
    except Exception as e:
        print(f"\nError al guardar los datos: {e}")


# ------------------------------------------------------------------------
# -------  MAIN PROGRAM ------
def main():

    while True:
        clear_console()
        show_menu()

        new_entry = []
        option_number = read_menu_option(1, 4)

        if option_number is None:
            input("\nPresione Enter para continuar...")
            continue

        if option_number == 1:
            clear_console()
            show_header("AGREGAR REGISTRO")
            new_entry = read_multiline_entry()
            save_file(new_entry, FILE_PATH)
            print(f"Entrada guardada exitosamente en: \n{FILE_PATH} \n")

        elif option_number == 2:
            clear_console()
            show_header("MOSTRANDO TODOS LOS REGISTROS")
            records = get_file_records()
            if not records:
                print("No hay registros guardados para mostrar.")
            else:
                for record in records:
                    print(f"{record}\n")

        elif option_number == 3:
            clear_console()
            show_header("BUSCAR POR PALABRA CLAVE")
            records = get_file_records()
            if not records:
                print("No hay registros guardados para buscar.")
            else:
                search_word = input("¿Qué palabra desea buscar?> ").strip()
                if not search_word:
                    print("No ha ingresado ninguna palabra para buscar.")
                else:
                    print("\nEntradas que coinciden con la búsqueda:\n")
                    for record in records:
                        if search_word.upper() in record.upper():
                            print(f"{record}\n")

        elif option_number == 4:
            print("\nHas salido del programa.")
            break

        input("\nEnter para volver al menú...")


if __name__ == "__main__":
    main()
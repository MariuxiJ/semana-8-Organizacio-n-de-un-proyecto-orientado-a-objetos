import os
import subprocess

class GestorConfiguracion:
    def __init__(self):
        # Identificadores y Tipos de Datos (String, Float)
        # Encapsulamiento Privado (__)
        self.__sistema = "Dashboard Académico Pro"
        self.__version = 3.5  # Dato tipo Float 
        self.__estudiante = "Mariuxi Shingre"
        #Estructuras Lógicas (Operadores de asignación)
        self.inicio_sesion = os.path.getctime(__file__) 

    def obtener_encabezado(self):
        # Operadores de Formato y Strings
        # Aplicamos Abstracción para mostrar un diseño profesional
        raya = "=" * 60  # Operador de repetición 
        return f"{raya}\n  {self.__sistema.upper()} | VERSIÓN: {self.__version}\n  USUARIO: {self.__estudiante}\n{raya}"

class GestorArchivos:
    def __init__(self):
        # Atributo Protegido (_)
        self._ruta_base = os.path.dirname(__file__)

    def mostrar_estado_proyecto(self):
        # Flujos de Control (Bucles y Condicionales)
        print(f"\n[SISTEMA] Escaneando ruta: {self._ruta_base}")
        
        # Usamos una lista para iterar
        for i in [1, 2]:
            u_path = os.path.join(self._ruta_base, f"Unidad {i}")
            
            # Estructura condicional IF/ELSE
            if os.path.exists(u_path):
                
                temas = [f for f in os.scandir(u_path) if f.is_dir()]
                cantidad = len(temas)
                # Operadores Relacionales (Comparación)
                estado = "COMPLETO" if cantidad > 0 else "VACÍO"
                print(f"   > Unidad {i}: {cantidad} temas ({estado})")
            else:
                print(f"   > Unidad {i}: No localizada.")

    def buscar_script_especifico(self, nombre_buscado):
        # Modularidad y Refactorización
        # Aplicamos búsqueda lógica y métodos de String 
        print(f"\n[BUSCADOR] Rastreando coincidencia para: '{nombre_buscado}'...")
        encontrados = []
        for raiz, dirs, archivos in os.walk(self._ruta_base):
            for archivo in archivos:
                # Métodos de String (.lower) y Operadores Lógicos (and)
                if nombre_buscado.lower() in archivo.lower() and archivo.endswith('.py'):
                    encontrados.append(os.path.join(raiz, archivo))
        return encontrados

def mostrar_codigo(ruta_script):
    
    ruta_script_absoluta = os.path.abspath(ruta_script)

    """
    Se añadió manejo de codificación UTF-8 
    y numeración de líneas para una lectura más técnica.
    """
    try:
        # Cambio: Se agregó encoding='utf-8' para evitar errores con tildes y caracteres especiales
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Visualizando: {ruta_script} ---")
            # Cambio: Se implementó un bucle con enumerate() para mostrar números de línea
            # Esto mejora la legibilidad comparado con el print() directo anterior
            for i, linea in enumerate(archivo, start=1):
                # Imprime el número de línea seguido del contenido
                print(f"{i} | {linea}", end="")
            return True
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}

    while True:
        print("\n" + "="*35)
        print("   MENU PRINCIPAL - DASHBOARD")
        print("="*35)
        
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("\nElige una unidad o '0' para salir: ")
        
        if eleccion_unidad == '0':
            print("Cerrando el sistema. ¡Hasta luego!")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    #Instanciación de los objetos con nombres descriptivos 
    configuracion = GestorConfiguracion()
    proyecto = GestorArchivos()
    
    # Mostramos el encabezado y el estado del proyecto
    # Esto usa el encapsulamiento para proteger  nombre y versión
    print(configuracion.obtener_encabezado())
    proyecto.mostrar_estado_proyecto()
    
    # Mensaje de control de flujo para el usuario
    print("\n[SISTEMA] Iniciando navegación de carpetas...")
    
    # Llamamos al menú principal para que el programa empiece a funcionar
    mostrar_menu()



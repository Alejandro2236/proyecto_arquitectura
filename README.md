# Simulador de Computadora

Este proyecto simula una computadora simple con componentes como la CPU, RAM, bus del sistema, registros, y más. El
proyecto está implementado en **Python** y tiene como objetivo simular las operaciones básicas de una computadora, como
la ejecución de instrucciones en un lenguaje ensamblador reducido.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **Modelos**: Representan los componentes de la computadora, como la CPU, RAM, registros, ALU, etc.
- **Controladores**: Gestionan las interacciones entre los componentes de la computadora.
- **Vistas**: Se encargan de la interfaz de usuario (si aplica).
- **Lectores**: Clases encargadas de leer y analizar el código ensamblador (SyntaxReader) y traducirlo a lenguaje de
  máquina (AssemblerReader).
- **Servicios**: Implementan la lógica de alto nivel, como la ejecución de instrucciones y la actualización de
  registros.

## Estilo de Código

Para mantener un estilo de código consistente en todo el proyecto, hemos utilizado un archivo `.editorconfig` que define
las reglas de formato. Este archivo se encuentra en la raíz del proyecto y es compatible con la mayoría de los editores
de texto, incluidos **PyCharm**, **Visual Studio Code**, y **Sublime Text**.

### Cómo formatear el código:

Si estás usando **PyCharm**, puedes formatear el código con el atajo:

- **Ctrl + Alt + L** (Windows/Linux)
- **Cmd + Alt + L** (macOS)

Esto aplicará automáticamente las configuraciones definidas en el archivo `.editorconfig`.

### Instrucciones para otros editores:

Si usas un editor diferente, asegúrate de que **EditorConfig** esté habilitado. Muchos editores, como **Visual Studio
Code** o **Sublime Text**, soportan **EditorConfig** de manera predeterminada o a través de un plugin.

## Estructura de Archivos

- Los **nombres de los paquetes** deben ser de una palabra, preferiblemente, o estar en **flatcase** si se requieren
  más de una.
    - **Ejemplo**:
        - **De una palabra**: models
        - **De más de una palabra**: unitofwork
- Cada **clase** debe estar en su propio archivo Python.
- El **nombre del archivo** debe coincidir con el nombre de la clase, pero todo en minúsculas y con guiones bajos
  **(snake_case)**.
    - **Ejemplo**: La clase **CPU** debe estar en el archivo **cpu.py**.
- El **nombre de la clase** debe estar en **Pascal Case**.
    - **Ejemplo**: class **CPU**:
- **No mezclar español e inglés** en el código:
    - **Variables, funciones, clases, documentación y comentarios** deben estar en **español**.
    - Usar nombres en inglés solo cuando el término sea estándar y ampliamente reconocido (como **CPU**, **RAM**,
      **ALU**).

## Convenciones de Commits

- Realiza **commits frecuentes**. Cada commit debe agregar una pequeña pero **funcional parte** del proyecto.
    - **Ejemplo**: Si implementas una nueva función, haz un commit para esa función específica.
- **Evita commits con cambios masivos**. No combines demasiadas modificaciones en un solo commit.
    - Si estás agregando una nueva funcionalidad o corrigiendo un error, haz un commit por cada parte del cambio.
- Asegúrate de usar **pull** para actualizar el proyecto antes de hacer un **push** para subir un cambio.
- **Siempre avisa cuando subas un commit**

## Formato de los Docstrings

El formato para los **docstrings** debe seguir la convención de **reStructuredText**.

- **Ejemplo de docstring**:
    ```python

    class CPU:
        """
        Representa la unidad central de procesamiento (CPU).

        :param registros: Lista de registros de propósito general.
        :type registros: list
        :param flags: Flags de la CPU (por ejemplo, cero, carry).
        :type flags: dict
        """
- Usa los docstrings para describir el propósito de cada clase, función y método.
- Para **parámetros** y **tipos de retorno**, usa el formato estándar de reStructuredText como se muestra en el ejemplo
  anterior.

## Organización del Código

- **Clases**: Cada clase debe tener su propia responsabilidad y debe ser independiente de otras.
- **Métodos**: Los métodos de cada clase deben estar claramente definidos. Asegúrate de que cada método tenga una única
  responsabilidad.
- **Funciones**: Las funciones auxiliares deben estar dentro de los módulos correspondientes y tener nombres claros en
  español.

## Uso de Comentarios

**Evita utilizar comentarios**. Intenta usar **docstrings**, **nombres de variables y funciones claros**, para que el
código se explique por sí mismo y no necesites usar comentarios.

Si necesitas usar comentarios:

- **Usa comentarios claros y breves** donde sea necesario para explicar partes del código que no sean obvias.
- **Evita comentarios redundantes**. El código debe ser lo suficientemente claro para que no se necesiten explicaciones
  innecesarias.
- Si usas **comentarios de bloque**, asegúrate de que sean relevantes y ayuden a entender partes complejas del código.

## Encapsulamiento

- **Todos los atributos** de las clases serán **privados o protegidos**, usando **doble guión bajo** para
  **los privados** (__privado) y **un único guión bajo** para **los protegidos** (_protegido).
- Para **los atributos que necesiten ser accedidos de forma pública**, se utilizará el decorador **@property**.
    ```python
    class Example:
    def __init__(self):
        self.__atributo = "valor"
    
    @property
    def atributo(self):
        return self.__atributo

- Al usar únicamente el decorador **@property**, el atributo será de tipo **read-only**. Para que sea totalmente
  público, se debe agregar el setter con **@nombre_de_la_propiedad.setter**.
    ```python
    @atributo.setter
    def atributo(self, atributo):
        self.__atributo = atributo

Con esto, el atributo también será editable públicamente.

- En caso de necesitar un atributo que sólo pueda editarse pero no leerse, se debera usar la siguiente estructura:
    ```python
    @property
    def atributo(self):
        raise AttributeError("El atributo no es accesible desde el exterior.")

    @atributo.setter
    def atributo(self, atributo):
        self.__atributo = atributo

## Ejemplo de Estructura de Archivos

```bash
simulated_computer/
├── main.py
├── modelos/
│   ├── __init__.py
│   ├── cpu.py               # Contiene la clase CPU
│   ├── ram.py               # Contiene la clase RAM
│   └── bus_sistema.py        # Contiene la clase Bus de sistema
├── controladores/
│   ├── __init__.py
│   └── controlador_simulacion.py  # Contiene la clase Controlador de simulación
├── servicios/
│   ├── __init__.py
│   └── ejecutor_instrucciones.py  # Contiene la clase Ejecutador de instrucciones
├── lectores/
│   ├── __init__.py
│   ├── lector_syntaxis.py     # Contiene la clase Lector de sintaxis
│   └── lector_ensamblador.py  # Contiene la clase Lector de ensamblador
├── vistas/
│   ├── __init__.py
│   └── vista_cliente.py          # Vista para la interfaz de línea de comandos
└── tests/
    ├── __init__.py
    ├── test_cpu.py          # Pruebas unitarias para la clase CPU
    ├── test_lector_syntaxis.py # Pruebas unitarias para SyntaxReader
    └── test_ejecutor_instrucciones.py  # Pruebas unitarias para InstructionExecutor
    
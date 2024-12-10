from dash import Dash, html, dcc, Input, Output
from threading import Thread
import time

from modelos.alu import ALU
from modelos.bus_control import BusControl
from modelos.bus_datos import BusDatos
from modelos.bus_direcciones import BusDirecciones
from modelos.memoria_datos import MemoriaDatos
from modelos.memoria_instrucciones import MemoriaInstrucciones
from modelos.monitor import DataMonitor
from modelos.psw import Psw
from modelos.ir import Ir
from modelos.mar import Mar
from modelos.mbr import Mbr
from modelos.pc import Pc
from modelos.unidad_control import UnidadControl
from modelos.unidad_control_cableada import UnidadControlCableada

# Asegúrate de que el archivo esté accesible.

# Instancia de la aplicación Dash
app = Dash(__name__)

# Instancia del DataMonitor
monitor = DataMonitor()

alu = ALU()
psw = Psw()
ir = Ir()
pc = Pc()
mar = Mar()
mbr = Mbr()
bus_direcciones = BusDirecciones()
bus_datos = BusDatos()
bus_control = BusControl()
memoria_instrucciones = MemoriaInstrucciones(128)
memoria_datos = MemoriaDatos(128)

mar.bus_direcciones = bus_direcciones
mbr.bus_datos = bus_datos
bus_datos.mbr = mbr
memoria_instrucciones.bus_control = bus_control
memoria_instrucciones.bus_direcciones = bus_direcciones
memoria_instrucciones.bus_datos = bus_datos

memoria_datos.bus_control = bus_control
memoria_datos.bus_direcciones = bus_direcciones
memoria_datos.bus_datos = bus_datos

unidad_control = UnidadControl()
unidad_control_cableada = UnidadControlCableada(
    pc,
    mar,
    mbr,
    bus_datos,
    bus_direcciones,
    bus_control,
    memoria_instrucciones,
    ir,
    unidad_control,
    psw,
    alu
)

monitor.add_model("ALU", alu)
monitor.add_model("PSW", psw)
monitor.add_model("IR",ir)
monitor.add_model("MAR",mar)
monitor.add_model("MBR",mbr)
monitor.add_model("PC",pc)
monitor.add_model("MEMORIAINSTRUCCIONES", memoria_instrucciones)
monitor.add_model("MEMORIADATOS", memoria_datos)
monitor.add_model("BUSDIRECCIONES", bus_direcciones)
monitor.add_model("BUSDATOS", bus_datos)
monitor.add_model("BUSCONTROL", bus_control)
monitor.add_model("UNIDADCONTROL", unidad_control)
monitor.add_model("UNIDADCONTROLCABLEADA", unidad_control_cableada)

def start_monitoring():
    monitor.monitor_changes()

thread = Thread(target=start_monitoring)
thread.daemon = True
thread.start()

# Layout de la aplicación
app.layout = html.Div(
    className="main-container",
    children=[
        # Contenedor ALU y controles
        html.Div(
            className="alu-and-controls-container",
            children=[
                # Contenedor ALU
                html.Div(
                    className="alu-container",
                    children=[
                        html.Div("ALU", className="alu-title"),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div("OPERANDO 1", className="alu-title-square"),
                                        dcc.Textarea(className="alu-square", id="operando-1", value=""),
                                    ],
                                    className="alu-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("OPERANDO 2", className="alu-title-square"),
                                        dcc.Textarea(className="alu-square", id="operando-2", value=""),
                                    ],
                                    className="alu-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("RESULTADO", className="alu-title-result"),
                                        dcc.Textarea(className="alu-result", id="resultado", value=""),
                                    ],
                                    className="alu-result-item",
                                ),
                            ],
                            className="alu-grid",
                        ),
                    ],
                ),
                # Contenedor PSW, PC, UNIDAD DE CONTROL, UNIDAD DE CONTROL CABLEADA
                html.Div(
                    className="control-units-container",
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div("PSW", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="psw", value=""),
                                    ],
                                    className="control-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("PC", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="pc", value=""),
                                    ],
                                    className="control-item",
                                ),
                            ],
                            className="control-left-column",
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div("UNIDAD DE CONTROL", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="unidad-control", value=""),
                                    ],
                                    className="control-item",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("UNIDAD DE CONTROL C", className="alu-title-square"),
                                        dcc.Textarea(className="control-square", id="unidad-control-c", value=""),
                                    ],
                                    className="control-item",
                                ),
                            ],
                            className="control-right-column",
                        ),
                    ],
                ),
            ],
        ),
        # MAR, MBR, IR y Banco de Registros
        html.Div(
            className="mar-mbr-ir-container",
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div("MAR", className="alu-title-square"),
                                dcc.Textarea(className="mar-mbr-ir-square", id="mar", value=""),
                            ],
                            className="mar-mbr-ir-item",
                        ),
                        html.Div(
                            children=[
                                html.Div("MBR", className="alu-title-square"),
                                dcc.Textarea(className="mar-mbr-ir-square", id="mbr", value=""),
                            ],
                            className="mar-mbr-ir-item",
                        ),
                        html.Div(
                            children=[
                                html.Div("IR", className="alu-title-square"),
                                dcc.Textarea(className="mar-mbr-ir-square", id="ir", value=""),
                            ],
                            className="mar-mbr-ir-item",
                        ),
                    ],
                    className="mar-mbr-ir-grid",
                ),
                html.Div(
                    className="bank-of-registers-container",
                    children=[
                        html.Div("BANCO DE REGISTROS", className="registers-title"),
                        dcc.Textarea(className="registers-square", id="banco-registros", value=""),
                    ],
                ),
                # Bloque para ingresar información
                html.Div(
                    className="bank-of-registers-container",
                    children=[
                        html.Div("Ingrese la Información", className="registers-title"),
                        dcc.Textarea(
                            className="info-square",
                            id="ingrese-informacion",
                            value="",
                            style={"resize": "none"},  # Evita el redimensionamiento
                        ),
                    ],
                ),
            ],
        ),
        # Buses
        html.Div(
            className="buses-container",
            children=[
                html.Div(
                    children=[
                        html.Div("BUS DE CONTROL", className="alu-title-square"),
                        dcc.Textarea(className="content-box", id="bus-control", value=""),
                    ],
                    className="bus",
                ),
                html.Div(
                    children=[
                        html.Div("BUS DE DATOS", className="alu-title-square"),
                        dcc.Textarea(className="content-box", id="bus-datos", value=""),
                    ],
                    className="bus",
                ),
                html.Div(
                    children=[
                        html.Div("BUS DE DIRECCIONES", className="alu-title-square"),
                        dcc.Textarea(className="content-box", id="bus-direcciones", value=""),
                    ],
                    className="bus",
                ),
            ],
        ),
        # Memorias y botones
        html.Div(
            className="memory-button-container",
            children=[
                html.Div(
                    className="memory-container",
                    children=[
                        html.Div("MEMORIAS", className="memory-title"),
                        html.Div(
                            id="memory-columns-container",
                            className="memory-columns-container",
                            children=[
                                html.Div(
                                    className="memory-column",
                                    children=[
                                        html.Div("Instrucciones", className="memory-subtitle"),
                                        html.Div(className="memory-content"),
                                    ],
                                ),
                                html.Div(
                                    className="memory-column",
                                    children=[
                                        html.Div("Datos", className="memory-subtitle"),
                                        html.Div(className="memory-content"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="button-container",
                    children=[
                        html.Button("Cargar", className="memory-button"),
                        html.Button("Ejecutar", className="memory-button"),
                        html.Button("Siguiente", className="memory-button"),
                    ],
                ),
            ],
        ),
        # Intervalo para disparar actualizaciones
        dcc.Interval(id="update-interval", interval=2000),  # Intervalo de 2 segundos
    ],
)

# Callback para actualizar los valores de la interfaz desde el DataMonitor
@app.callback(
    [
        Output("operando-1", "value"),
        Output("operando-2", "value"),
        Output("resultado", "value"),
        Output("mar", "value"),
        Output("mbr", "value"),
        Output("ir", "value"),
    ],
    [Input("update-interval", "n_intervals")]
)
def update_values(n_intervals):
    # Extraer los cambios del monitor
    changes = monitor.get_changes()

    # Valores predeterminados para cada componente
    values = {
        "operando_1": "",
        "operando_2": "",
        "resultado": "",
        "mar": "",
        "mbr": "",
        "ir": "",
    }

    # Aplicar los cambios obtenidos
    for name, data in changes:
        if name == "ALU":
            values["operando_1"] = data.get("operando_1", "")
            values["operando_2"] = data.get("operando_2", "")
            values["resultado"] = data.get("resultado", "")
        elif name == "MAR":
            values["mar"] = data.get("value", "")
        elif name == "MBR":
            values["mbr"] = data.get("value", "")
        elif name == "IR":
            values["ir"] = data.get("value", "")

    return (
        values["operando_1"],
        values["operando_2"],
        values["resultado"],
        values["mar"],
        values["mbr"],
        values["ir"],
    )

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)

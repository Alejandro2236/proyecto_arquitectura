from threading import Timer
from queue import Queue

class DataMonitor:
    def __init__(self, refresh_interval=5):
        self.models = {}
        self.changes = Queue()
        self.refresh_interval = refresh_interval  # Intervalo en segundos para actualizar la vista
        self.timer = None

    def add_model(self, name, model):
        """Añadir un modelo para monitorear."""
        self.models[name] = model

    def monitor_changes(self):
        """Revisar si hay cambios en los modelos."""
        for name, model in self.models.items():
            # Supongamos que cada modelo tiene un método `to_dict` para extraer sus datos.
            data = model.to_dict()
            if hasattr(model, "_last_data") and model._last_data != data:
                self.changes.put((name, data))
            model._last_data = data

        # Reiniciar el temporizador
        self.timer = Timer(self.refresh_interval, self.monitor_changes)
        self.timer.start()

    def get_changes(self):
        """Obtener todos los cambios acumulados en la cola."""
        changes = []
        while not self.changes.empty():
            changes.append(self.changes.get())
        return changes

    def stop_monitoring(self):
        """Detener la monitorización."""
        if self.timer:
            self.timer.cancel()

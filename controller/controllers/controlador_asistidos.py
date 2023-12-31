from controller.controllers.controlador_eventos import ControladorEventos


class ControladorAsistidos(ControladorEventos):
    def __init__(self, app):
        super().__init__(app)

    def obtener_eventos_asistidos(self):
        eventos_asistidos = self.obtener_usuario_actual().historial_eventos
        return [self.obtener_evento_id(id_evento) for id_evento in eventos_asistidos]
# main.py
from kivy.config import Config

# Configurar Kivy para usar OpenGL estándar
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'borderless', '1')
# No forzar OpenGL ES 2.0

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image

from app.core.object_detector import ObjectDetector
from app.core.camera import Camera

class MainApp(App):
    def build(self):
        self.detector = ObjectDetector()  # Inicializar el detector de objetos
        self.camera = Camera()            # Inicializar la cámara
        self.img_widget = Image()         # Widget de imagen para mostrar la cámara

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.img_widget)

        # Actualiza la imagen de la cámara cada 1/30 segundos
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return layout

    def update(self, dt):
        # Captura una imagen desde la cámara
        frame = self.camera.get_frame()

        # Realiza la detección de objetos
        detections, image_with_detections = self.detector.detect_objects(frame)

        # Convertir la imagen para mostrarla en Kivy
        buf = image_with_detections.tobytes()
        texture = Texture.create(size=(image_with_detections.shape[1], image_with_detections.shape[0]))
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img_widget.texture = texture

if __name__ == '__main__':
    MainApp().run()

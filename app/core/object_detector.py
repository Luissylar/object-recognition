import tensorflow as tf
import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        # Cargar el modelo de detección de objetos
        self.model = tf.saved_model.load('assets/models/ssd_mobilenet_v2_fpnlite_320x320/saved_model')
        self.category_index = {1: 'persona', 2: 'bicicleta', 3: 'coche', 62: 'silla', 63: 'sofá', 64: 'mesa'}

    def detect_objects(self, image):
        # Preprocesamiento de la imagen
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis, ...]

        # Realiza la detección
        detections = self.model(input_tensor)

        # Procesa las detecciones
        detections = {key: value.numpy() for key, value in detections.items()}

        # Dibuja las detecciones en la imagen
        image_with_detections = self.draw_detections(image, detections)

        return detections, image_with_detections

    def draw_detections(self, image, detections):
        # Extraer información de las detecciones
        for i in range(int(detections['num_detections'][0])):
            score = detections['detection_scores'][0][i]
            if score > 0.5:  # Umbral de confianza
                class_id = int(detections['detection_classes'][0][i])
                bbox = detections['detection_boxes'][0][i]

                # Convertir coordenadas del cuadro delimitador
                h, w, _ = image.shape
                ymin, xmin, ymax, xmax = bbox
                left, right, top, bottom = int(xmin * w), int(xmax * w), int(ymin * h), int(ymax * h)

                # Dibujar el cuadro y la etiqueta
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                label = self.category_index.get(class_id, 'N/A')
                cv2.putText(image, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return image

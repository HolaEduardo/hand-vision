# Proyecto de Control y Detección con Manos
Autor: Eduardo Jara.
Este proyecto utiliza **MediaPipe Hands**, **OpenCV** y **pynput** para realizar diferentes funcionalidades relacionadas con el rastreo y la detección de manos a través de una cámara web. Incluye control de teclado basado en la orientación de la palma, detección de agarre de objetos y conteo de dedos levantados.

## Características

- **Control de Orientación de la Mano**: Emula las teclas `W`, `A`, `S`, `D` según la inclinación y el giro de la palma.
- **Detección de Agarre de Objetos**: Identifica si la mano está agarrando un objeto basándose en las distancias entre puntos clave de la mano.
- **Conteo de Dedos Levantados**: Detecta y muestra en pantalla la cantidad de dedos levantados.

## Requisitos

- Python 3.12 o superior
- OpenCV
- MediaPipe
- NumPy
- pynput

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd <carpeta-del-repositorio>
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Asegúrate de que tu cámara web esté conectada y funcionando.

## Uso

### Control de Orientación de la Mano

Archivo: `hand_track.py`

1. Ejecuta el script:
   ```bash
   python hand_track.py
   ```

2. Controla las teclas de dirección con la orientación de tu mano:
   - Inclinación hacia adelante: `W`
   - Inclinación hacia atrás: `S`
   - Giro hacia la izquierda: `A`
   - Giro hacia la derecha: `D`

3. Presiona `Q` para salir.

### Detección de Agarre de Objetos

Archivo: `object_grip.py`

1. Ejecuta el script:
   ```bash
   python object_grip.py
   ```

2. El programa mostrará en pantalla:
   - "Agarrando objeto" si detecta un agarre.
   - "No en agarre" si no detecta un agarre.

3. Presiona `Q` para salir.

### Conteo de Dedos Levantados

Archivo: `fingers_count.py`

1. Ejecuta el script:
   ```bash
   python fingers_count.py
   ```

2. El programa mostrará en pantalla la cantidad de dedos levantados detectados.

3. Presiona `Q` para salir.

## Estructura del Proyecto

- `hand_track.py`: Control de teclado basado en la orientación de la mano.
- `object_grip.py`: Detección de agarre de objetos.
- `fingers_count.py`: Conteo de dedos levantados.
- `README.md`: Documentación del proyecto.
- `requirements.txt`: Lista de dependencias necesarias.

## Notas

- Asegúrate de tener buena iluminación para mejorar la detección de la mano.
- Los scripts están configurados para detectar una sola mano a la vez.
- Los umbrales de detección pueden ajustarse en los scripts según sea necesario.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

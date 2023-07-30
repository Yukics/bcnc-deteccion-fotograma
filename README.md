# Reconocimiento de fotogramas en un vídeo

**Entrevista técnica BCNC**

## Requisitos previos

+ Python 3.11
+ Git
+ Probado en Windows 11

## Puesta en marcha

1. Clonar el repositorio

    ```powershell
    git clone https://github.com/Yukics/bcnc-deteccion-fotograma.git
    ```

2. Iniciar virtual env

    ```powershell
    .\env\Scripts\activate
    ```

3. Instalar posibles dependencias

    ```powershell
    python -m ensurepip
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Localizar un vídeo y recoger un fotograma o imagen que aparezca en este. O simplemente utilizar los ubicados en la carpeta `media`.

5. Localizar el fotograma exacto en el que aparece utilizando el siguiente comando:
    + `-v`: Ubicación del vídeo
    + `-i`: Ubicación de la imagen o fotograma

    ```powershell
    py .\main.py -i ./media/prueba.png -v ./media/prueba.mp4
    ```

## Especificación

Necesitamos un vídeo (testeado con 2 mp4) y una imagen (testeado con png), de no encontrarse dentro del vídeo es probable que no se muestre nada por pantalla y la ejecución del script se detenga automáticamente.

## Inicialización del proyecto y comandos de utilidad

Instalación de virtualenv:

```powershell
py -m pip install --user virtualenv
```

Creación del virtual environment:

```powershell
py -m venv env
```

Activar virtual environment:

```powershell
.\env\Scripts\activate
```

Instalación de paquetes necesarios, ej:

```powershell
py -m pip install requests opencv-python
```

Generación del requirements.txt:

```powershell
py -m pip freeze > requirements.txt
```

Instalación desde el requirements.txt:

```powershell
pip install -r requirements.txt
```

Desactivar el virtual environment:

```powershell
deactivate
```

## Mejoras implementadas

Al comenzar el proyecto tuve en cuenta que posiblemente un futuro requisito podría ser el reconocimiento de cualquier parte de fotograma. Por lo que utilice directamente el método de OpenCV `.matchTemplate`.

## Posibles Mejoras

Dependiendo de la resolución de pantalla, es posible que la imagen template no encaje correctamente con el frame del video. Por lo que se podría realizar un escalado a la baja del frame, para hacerlo coincidir con la escala de la imagen a reconocer. Debido al overhead de cómputo que esto iba a suponer y tiempo dedicado decidí priorizar una segunda prueba en la que mostrar otro abanico de conocimientos.

## Referencias

+ Venv [https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

Origen de los videos de pruebas sin copyright: 
+ [https://www.pexels.com/video/light-road-dawn-landscape-16343098/](https://www.pexels.com/video/light-road-dawn-landscape-16343098/)
+ [https://www.pexels.com/video/people-walking-in-the-snow-6431722/](https://www.pexels.com/video/people-walking-in-the-snow-6431722/)

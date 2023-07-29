# Reconocimiento de fotogramas en un vídeo

**Entrevista técnica BCNC**

## Requisitos previos

+ Python 3.11
+ Git

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

4. Localizar un vídeo y recoger un fotograma o imagen que aparezca en este.

5. Localizar el fotograma exacto en el que aparece utilizando el siguiente comando

    ```powershell
    py .\main.py -i ./media/prueba.png -v ./media/video.mp4
    ```

Necesitamos un vídeo (testeado con 2 mp4) y una imagen (testeado con png), de no encontrarse dentro del vídeo es probable que no se muestre nada por pantalla y la ejecución del script se detenga automáticamente.

El programa necesita dos argumentos, la imagen que queremos encontrar dentro del vídeo y el vídeo en cuestión. Una vez activado el virtualenv (detalles de como hacerlo más abajo), ej:

```powershell
(env) PS C:\Users\yuki\Documents\repos\bcnc-deteccion-fotograma> py main.py -i ./media/prueba.png -v ./media/video.mp4
```

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

Instalación de paquetes necesarios:

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

De la forma en la que planificaba desde un principio el proyecto decidí que sería posible que un requisito más adelante podría ser detectar alguna parte de un fotograma por lo que la implementación del reconocimiento de la imagen también es capaz de detectar 

## Posibles Mejoras

Dependiendo de la resolución de pantalla es posible que la imagen template no encaje correctamente con el frame del video por lo que se podría realizar un escalado a la baja del frame para hacerlo coincidir correctamente independientemente de la resolución original del video.

## Referencias

+ Venv [https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

## Miscelaneas

+ Ryzen 5900x
+ RAM 64GB
+ Windows 11
+ Python 3.10

Origen de los videos de pruebas sin copyright: 
+ [https://www.pexels.com/video/light-road-dawn-landscape-16343098/](https://www.pexels.com/video/light-road-dawn-landscape-16343098/)
+ [https://www.pexels.com/video/people-walking-in-the-snow-6431722/](https://www.pexels.com/video/people-walking-in-the-snow-6431722/)

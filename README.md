# Reconocimiento de fotogramas en un vídeo

### Entrevista técnica BCNC

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

## Referencias

+ Venv [https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

## Miscelaneas

Ordenador utilizado:

+ Ryzen 5900x
+ RAM 64GB
+ Windows 11
+ Python 3.10

Origen del video de pruebas sin copyright: [https://www.pexels.com/video/people-walking-in-the-snow-6431722/](https://www.pexels.com/video/people-walking-in-the-snow-6431722/)
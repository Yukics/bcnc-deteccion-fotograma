import logging
import cv2
import numpy as np
import os

def startRecon(video, image):
    logging.info("Comenzando el proceso de reconocimiento durante el video")

    try:
        # Cargamos el video
        vidcap = cv2.VideoCapture(video)
        # Cargamos la captura de alguno de los frames 
        template = cv2.imread(image,0) 

    except:
        logging.error("No ha sido posible cargar o el video o la imagen proporcionadas, revisa el path")
    
    # Contador para saber en que frame estamos iterando
    count = 0 

    # Mientras vidcap nos deje leer el stream de video realizaremos las siguientes acciones
    while (vidcap.isOpened()): 
      # Leemos un frame
      success, image = vidcap.read() 
      
      if not success: 
        # Si dejamos de poder leer el vídeo paramos
        logging.warning('Algo ha fallado a la hora leer un fotograma o ha finalizado el procesamiento del video')
        break         

      # Comparamos nuestra captura con el frame del video
      processImage(image, template, count) 
      count += 1

def processImage(frame, template, count):
    
    # Convertimos de rgb a escala de grises el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Medimos el ancho y alto del frame
    w,h = template.shape[0], template.shape[1]
    
    # Comprobamos que la captura está en el fotograma
    matched = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    
    # Establecemos el grado de fiabilidad necesario de 0 min a 1 max, 99.9% en este caso necesario
    threshold = .999
    
    # Aplicamos el grado de fiabilidad al resultado de la comprobación de la captura en el frame
    loc = np.where( matched >= threshold)
    
    # Cuando comprobamos el grado de fiabilidad, y existe una coincidencia casi exacta, estas arrays no estarán vacías
    if np.any(loc[0]) and np.any(loc[1]):
        logging.info('Localizada coincidencia con el frame n {}'.format(count))
        
        # Procedemos a generar el recuadro y a mostrar por pantalla la coincidencia ademas de al directorio processed
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

        # Si no existe el directorio processed lo creamos
        if not os.path.exists("./processed"):
            os.makedirs("./processed")

        # Escribimos la imagen en el disco con el recuadro de la coincidencia
        cv2.imwrite('./processed/res{0}.png'.format(count),frame)

        # Cambiamos el tamaño de la imagen que aparecerá por pantalla
        imS = cv2.resize(frame, (960, 540)) 

        # Mostramos por pantalla la imagen
        cv2.imshow('Frame n {}'.format(count) ,imS)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
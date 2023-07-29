import logging
import cv2
import numpy as np
import os

def startRecon(video, image):

    try:
        vidcap = cv2.VideoCapture(video) # Cargamos el video
        template = cv2.imread(image,0) # Cargamos la imagen
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    except:
        logging.error("No ha sido posible cargar o el video o la imagen proporcionadas, revisa el path")

    count = 0

    while True:
      success, image = vidcap.read()
      
      if not success: 
        logging.error('Algo ha fallado a la hora leer un fotograma')
        break         # Si dejamos de poder leer el vídeo paramos

    #   logging.info('Read a new frame: {} {}'.format(success, count))
      processImage(image, template, count)
      count += 1

def processImage(img_rgb, template, count):

    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = template
    # large_image = img_rgb
    large_image = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    print(small_image, large_image)

    result = cv2.matchTemplate(small_image, large_image, method)
    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    cv2.imshow('output',large_image)

    # The image is only displayed if we call this
    cv2.waitKey(0)











    # img_gray = img_rgb
    # # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    # w, h = template.shape[::-1]

    # res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    # threshold = 0.8
    # loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    # if not os.path.exists('processing'):
    #     os.makedirs('processing')

    # # This will write different res.png for each frame. Change this as you require
    # cv2.imwrite('./processing/res{0}.png'.format(count),img_rgb)   
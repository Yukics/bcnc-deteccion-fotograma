# Custom modules
import lib.logs as logs
import lib.recognize as recognize

# Generic modules
import logging
import sys
import argparse

def main():
    
    # Implementamos el logging
    logs.setupLogging()

    # Uso de argumentos pasados por cli
    parser = argparse.ArgumentParser(
        prog="photogram-recognizer",
        description='Muestra el fotograma exacto en el que aparezca la imagen pasada como parametro',
        epilog="Gracias por usar %(prog)s! :)",
    )
    parser.add_argument("-i", "--image")
    parser.add_argument("-v", "--video")

    args = parser.parse_args()

    if not args.image or not args.video:
        logging.warning('No se han pasado los argumentos necesarios para seguir la ejecución')
        sys.exit(1)

    recognize.startRecon(args.video, args.image)

if __name__ == '__main__':
    main()
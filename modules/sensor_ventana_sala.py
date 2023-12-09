""" import RPi.GPIO as GPIO
import time
import modules.envio_correos as envio_correos


def detectar_ventana():
    led_pin = 11
    pulsador_encendido_pin = 7
    pulsador_apagado_pin = 18

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulsador_encendido_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pulsador_apagado_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led_pin, GPIO.OUT)

    led_encendido = False

    try:
        while True:
            if GPIO.input(pulsador_encendido_pin) == GPIO.LOW:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                time.sleep(0.1)
                envio_correos.envio_correos()

            if GPIO.input(pulsador_apagado_pin) == GPIO.LOW:
                GPIO.output(led_pin, GPIO.LOW)
                led_encendido = False

    except KeyboardInterrupt:
        GPIO.cleanup()



detectar_ventana() """

import RPi.GPIO as GPIO
import time
import modules.envio_correos as envio_correos


def detectar_ventana():
    led_pin = 11
    pulsador_encendido_pin = 7
    pulsador_apagado_pin = 18

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulsador_encendido_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(pulsador_apagado_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(led_pin, GPIO.OUT)

    led_encendido = False

    try:
        while True:
            if GPIO.input(pulsador_encendido_pin) == GPIO.HIGH:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                time.sleep(0.1)
                envio_correos.envio_correos()

            if GPIO.input(pulsador_apagado_pin) == GPIO.HIGH:
                GPIO.output(led_pin, GPIO.LOW)
                led_encendido = False

    except KeyboardInterrupt:
        GPIO.cleanup()



detectar_ventana()

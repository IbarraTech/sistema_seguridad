import RPi.GPIO as GPIO
import time
import modules.envio_correos as envio_correos


def detectar_ventana():
    led_pin = 11
    pulsador_encendido_pin = 7
    pulsador_apagado_pin = 18
    sensor1_pin = 12
    sensor2_pin = 13
    sensor3_pin = 16
    sensor4_pin = 15

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulsador_encendido_pin, GPIO.IN)
    GPIO.setup(pulsador_apagado_pin, GPIO.IN)
    GPIO.setup(sensor1_pin, GPIO.IN)
    GPIO.setup(sensor2_pin, GPIO.IN)
    GPIO.setup(sensor3_pin, GPIO.IN)
    GPIO.setup(sensor4_pin, GPIO.IN)
    GPIO.setup(led_pin, GPIO.OUT)

    led_encendido = False

    try:
        while True:
            if GPIO.input(pulsador_encendido_pin) == GPIO.HIGH and not led_encendido:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                time.sleep(0.1)
                envio_correos.envio_correos()

            elif GPIO.input(pulsador_apagado_pin) == GPIO.HIGH and led_encendido:
                GPIO.output(led_pin, GPIO.LOW)
                led_encendido = False

            elif GPIO.input(sensor1_pin) == GPIO.HIGH and not led_encendido:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                time.sleep(0.1)
                envio_correos.envio_correos()

            elif GPIO.input(sensor2_pin) == GPIO.HIGH and not led_encendido:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                time.sleep(0.1)
                envio_correos.envio_correos()

            elif GPIO.input(sensor3_pin) == GPIO.HIGH and not led_encendido:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                time.sleep(0.1)
                envio_correos.envio_correos()

            elif GPIO.input(sensor4_pin) == GPIO.HIGH and not led_encendido:
                GPIO.output(led_pin, GPIO.HIGH)
                led_encendido = True
                time.sleep(0.1)
                envio_correos.envio_correos()

            elif led_encendido:
                GPIO.output(led_pin, GPIO.LOW)
                led_encendido = False

    except KeyboardInterrupt:
        GPIO.cleanup()


detectar_ventana()

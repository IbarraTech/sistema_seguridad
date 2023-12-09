import threading
import modules.sensor_ventana_sala as sensor_ventana_sala
import modules.sensor_ventana_habitacion as sensor_ventana_habitacion

# Crear hilos para cada módulo
thread_sala = threading.Thread(target=sensor_ventana_sala.detectar_ventana)
thread_habitacion = threading.Thread(
    target=sensor_ventana_habitacion.detectar_habitacion)

# Iniciar los hilos
thread_sala.start()
thread_habitacion.start()

# Esperar a que ambos hilos terminen (opcional)
thread_sala.join()
thread_habitacion.join()

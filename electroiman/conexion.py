
import serial
import time

# Configura la conexión serial
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

def verificar_conexion (puerto_serial):
    try:
        # Establecer la conexión con el Arduino
        ser = serial.Serial(puerto_serial, 9600, timeout=1)
        
        # Verificar si la conexión es exitosa
        if ser.is_open:
            print("Conexión establecida con éxito")
            return True
        else:
            print("No se pudo establecer la conexión")
            return False
    except serial.SerialException as e:
        print("Error al establecer la conexión:", e)
        return False

# Ejemplo de uso
puerto_serial = "COM3"  # Cambia por el puerto serial correcto
if verificar_conexion(puerto_serial):
    print("Conexión exitosa")
else:
    print("No se pudo establecer la conexión")

# Función para enviar comandos al Arduino
def send_command(command):
    arduino.write(command.encode())
    time.sleep(0.1)
    response = arduino.readline().decode().strip()
    return response

# Ejemplo de comandos
# Cambia al modo remoto
send_command('MODO_REMOTO')

# Ajusta la corriente (0-15 Vdc, ajusta según lo que necesita el inversor)
send_command('CORRIENTE:10')  # Por ejemplo, 10 V

# Envía señal TTL si se requiere
send_command('TTL_SIGNAL')

# Cierra la conexión al final
arduino.close()

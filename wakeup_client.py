import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)

# Configuración del broker MQTT
broker = 'localhost'
port = 1883
topic = 'test/topic'

# Variable global para el temporizador
message_timer = None

# Función para manejar el temporizador
def on_timeout():
	global communication_failed
	communication_failed = True

	print("FALLO LA COMUNICACION")

	reset_timer()  # Reinicia el temporizador para volver a verificar en 15 segundos

def reset_timer():
    global message_timer
    if message_timer:
        message_timer.cancel()
    message_timer = threading.Timer(15.0, on_timeout)
    message_timer.start()

def on_connect(client, userdata, flags, rc, properties=None):
	print("Connected with reason_code: " + str(rc))

	if rc != 0 :
		print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
	else:
		client.subscribe(topic)

def on_message(client, userdata, msg):
	print(f"Mensaje recibido en el tópico {msg.topic}: {msg.payload.decode()}")
	reset_timer()  # Reiniciar el temporizador cuando se recibe un mensaje

def on_subscribe(client, obj, mid, reason_code_list, properties):
	print("Subscribed: " + str(mid) + " " + str(reason_code_list))


def on_log(client, obj, level, string):
	print(string)

def main():
	nCount = 1

	client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
	# client = mqtt.Client()

	client.on_message = on_message
	client.on_connect = on_connect
	client.on_subscribe = on_subscribe

	# Uncomment to enable debug messages
	# mqttc.on_log = on_log
	client.connect(broker, port)
	
	print(f"Hola nCount")

	reset_timer()  # Iniciar el temporizador cuando se conecta

	# Mantenerse en escucha de mensajes
	client.loop_forever()

if __name__ == '__main__':
	main()

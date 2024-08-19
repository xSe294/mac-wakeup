import paho.mqtt.client as mqtt
import time


# Configuración del broker MQTT
broker = '127.0.0.1'
port = 1883
topic = 'test/topic'

# Crear instancia del cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def main():
	# Conectar al broker
	client.connect(broker, port)

	# Publicar un mensaje cada 5 segundos
	try:
		while True:
			message = "Hello, MQTT!"
			client.publish(topic, message)
			print(f"Mensaje enviado: {message}")
			time.sleep(5)
	except KeyboardInterrupt:
		print("Desconectando del broker MQTT")
		client.disconnect()

if __name__ == '__main__':
	main()

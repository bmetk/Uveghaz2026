import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

R1 = 16
R2 = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(R1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(R2, GPIO.OUT, initial=GPIO.HIGH)

def on_connect(client, userdata, flags, rc, properties=None):
	if rc == 0:
		client.subscribe("greenhouse/ventilation", qos=1)

def on_message(client, userdata, message):
	try:
        	msg = str(message.payload.decode("utf-8"))
        	if msg == "true":
                	print("Ventilátor bekapcsolva!")
                	GPIO.output(R1, GPIO.LOW)
                	GPIO.output(R2, GPIO.LOW)
        	elif msg == "false":
                	print("Ventilátor kikapcsolva!")
                	GPIO.output(R1, GPIO.HIGH)
                	GPIO.output(R2, GPIO.HIGH)
	except Exception as e:
		print(f"Hiba az üzenet feldolgozásakor: {e}", flush=True)

try:
	client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
	client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.loop_start()

try:
	client.connect("localhost", 1883, 60)
except Exception:
	pass

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print("\nLeállítás...")
finally:
	client.loop_stop()
	client.disconnect()
	GPIO.cleanup()
	print("Program leállítva.")

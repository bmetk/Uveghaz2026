import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

pump = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(pump, GPIO.OUT, initial=GPIO.HIGH)

def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
                client.subscribe("greenhouse/pump", qos=1)

def on_message(client, userdata, message):
	try:
		msg = str(message.payload.decode("utf-8"))
		if msg == "true":
			print("Pumpa bekapcsolva!")
			GPIO.output(pump, GPIO.LOW)
		elif msg == "false":
			print("Pumpa kikapcsolva!")
			GPIO.output(pump, GPIO.HIGH)
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

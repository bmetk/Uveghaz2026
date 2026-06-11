import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

left_lamp = 26
middle_lamp = 6
right_lamp = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_lamp, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(middle_lamp, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(right_lamp, GPIO.OUT, initial=GPIO.HIGH)

def on_connect(client, userdata, flags, rc, properties=None):
	if rc == 0:
		client.subscribe("greenhouse/leftlamp", qos=1)
		client.subscribe("greenhouse/middlelamp", qos=1)
		client.subscribe("greenhouse/rightlamp", qos=1)

def on_message(client, userdata, message):
	try:
		msg = str(message.payload.decode("utf-8"))
		if message.topic == "greenhouse/leftlamp":
			if msg == "true":
				GPIO.output(left_lamp, GPIO.LOW)
			elif msg == "false":
				GPIO.output(left_lamp, GPIO.HIGH)
		elif message.topic == "greenhouse/middlelamp":
			if msg == "true":
				GPIO.output(middle_lamp, GPIO.LOW)
			elif msg == "false":
				GPIO.output(middle_lamp, GPIO.HIGH)
		elif message.topic == "greenhouse/rightlamp":
			if msg == "true":
				GPIO.output(right_lamp, GPIO.LOW)
			elif msg == "false":
				GPIO.output(right_lamp, GPIO.HIGH)
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
        client.connect("192.168.10.193", 1883, 60)
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

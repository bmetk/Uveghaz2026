import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

# Pin definíciók (BCM számozás)
ENA = 18
ENB = 19
IN1, IN2 = 23, 24
IN3, IN4 = 25, 8

GPIO.setmode(GPIO.BCM)
GPIO.setup([ENA, ENB, IN1, IN2, IN3, IN4], GPIO.OUT)

# Irány beállítása (hogy a táp átmenjen a kimenetekre)
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)

# PWM inicializálása 100Hz-en (villogásmentes fényhez)
purple_light = GPIO.PWM(ENA, 100)
yellow_light = GPIO.PWM(ENB, 100)

purple_light.start(0) # 0% fényerővel indul
yellow_light.start(0)

def on_connect(client, userdata, flags, rc, properties=None):
	if rc == 0:
		client.subscribe("greenhouse/yellowlight", qos=1)
		client.subscribe("greenhouse/purplelight", qos=1)

def on_message(client, userdata, message):
	try:
		brightness = float(message.payload.decode("utf-8"))

		if message.topic == "greenhouse/yellowlight":
			yellow_light.ChangeDutyCycle(brightness)
		elif message.topic == "greenhouse/purplelight":
			purple_light.ChangeDutyCycle(brightness)
	except Exception as e:
		print(f"Váratlan hiba az üzenet feldolgozásakor: {e}", flush=True)

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
	purple_light.stop()
	yellow_light.stop()
	GPIO.cleanup()
	print("Program leállítva.")

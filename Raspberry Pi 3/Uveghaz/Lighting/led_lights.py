import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

# Pin definíciók (BCM számozás)
ENA_R = 18
ENB_R = 19
ENA_L = 25
ENB_L = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup([ENA_R, ENB_R, ENA_L, ENB_L], GPIO.OUT)

# PWM inicializálása 100Hz-en (villogásmentes fényhez)
purple_light_r = GPIO.PWM(ENA_R, 100)
yellow_light_r = GPIO.PWM(ENB_R, 100)
purple_light_l = GPIO.PWM(ENA_L, 100)
yellow_light_l = GPIO.PWM(ENB_L, 100)

purple_light_r.start(0) # 0% fényerővel indul
purple_light_l.start(0)
yellow_light_r.start(0)
yellow_light_l.start(0)

def on_connect(client, userdata, flags, rc, properties=None):
	if rc == 0:
		client.subscribe("greenhouse/yellowlight", qos=1)
		client.subscribe("greenhouse/purplelight", qos=1)

def on_message(client, userdata, message):
	try:
		brightness = float(message.payload.decode("utf-8"))

		if message.topic == "greenhouse/yellowlight":
			yellow_light_r.ChangeDutyCycle(brightness)
			yellow_light_l.ChangeDutyCycle(brightness)
		elif message.topic == "greenhouse/purplelight":
			purple_light_r.ChangeDutyCycle(brightness)
			purple_light_l.ChangeDutyCycle(brightness)
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
	purple_light_r.stop()
	purple_light_l.stop()
	yellow_light_r.stop()
	yellow_light_l.stop()
	GPIO.cleanup()
	print("Program leállítva.")

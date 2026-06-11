import pigpio
import time
import paho.mqtt.client as mqtt

SERVO = 17

pi = pigpio.pi()
if not pi.connected:
	print("A pigpiod nem fut!")

def on_connect(client, userdata, flags, rc, properties=None):
	if rc == 0:
		client.subscribe("greenhouse/backwindow", qos=1)

def on_message(client, userdata, message):
	if not pi.connected:
		print("A pigpiod nem elérhető!")
		return
	try:
		msg = str(message.payload.decode("utf-8"))
		if msg == "true":
			print("Hátsó ablak kinyitva!", flush=True)
			pi.set_servo_pulsewidth(SERVO, 2400)
			time.sleep(2)
			pi.set_servo_pulsewidth(SERVO, 0)
		elif msg == "false":
			print("Hátsó ablak becsukva!", flush=True)
			for i in range(2400, 1500, -10):
				pi.set_servo_pulsewidth(SERVO, i)
				time.sleep(0.01)
			time.sleep(0.1)
			pi.set_servo_pulsewidth(SERVO, 0)
	except Exception as e:
		print(f"Hiba történt a szervó vezérlése közben: {e}", flush=True)

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
	if pi.connected:
		pi.set_servo_pulsewidth(SERVO, 0)
		pi.stop()
		print("Szervó vezérlő leállítva.")

import time
import board
import busio
import json
import paho.mqtt.client as mqtt
import adafruit_sgp30

# MQTT Connection
try:
	client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
	client = mqtt.Client()

client.loop_start()

try:
	client.connect("localhost", 1883, 60)
except Exception:
	pass

# Sensor Initialization
i2c = busio.I2C(board.SCL, board.SDA)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

sgp30.iaq_init()
# SGP30 Baseline values setting
sgp30.set_iaq_baseline(34041, 36491)

try:
	while True:
		co2, tvoc = sgp30.iaq_measure()

		payload = {
			"co2_ppm": co2,
			"tvoc_ppb": tvoc
		}

		# Sending Data
		try:
			client.publish("greenhouse/sensors", json.dumps(payload), qos=1)
			print(f"Adat elküldve: {payload}", flush = True)
			# print(f"eCO2_B: {sgp30.baseline_eCO2} TVOC_B:{sgp30.baseline_TVOC}", flush = True)
		except Exception:
			pass

		time.sleep(5)

except KeyboardInterrupt:
	print("\nLeállítás...")
finally:
	client.loop_stop()
	client.disconnect()

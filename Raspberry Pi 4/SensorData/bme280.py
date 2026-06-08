import time
import board
import busio
import json
import paho.mqtt.client as mqtt
from adafruit_bme280 import basic as adafruit_bme280

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
bme280_1 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
bme280_2 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)

try:
	while True:
		temp_1 = bme280_1.temperature
		hum_1 = bme280_1.humidity
		pres_1 = bme280_1.pressure
		temp_2 = bme280_2.temperature
		hum_2 = bme280_2.humidity
		pres_2 = bme280_2.pressure

		payload = {
			"légnyomás": round((pres_1 + pres_2) /2, 1),
			"hőmérséklet": round((temp_1 + temp_2) /2, 2),
			"páratartalom": round((hum_1 + hum_2) /2, 1)
		}

		# Sending Data
		try:
			client.publish("greenhouse/sensors", json.dumps(payload), qos=1)
			print(f"Adat elküldve: {payload}", flush = True)
		except Exception:
			pass
		time.sleep(5)

except KeyboardInterrupt:
	print("\nLeállítás...")
finally:
	client.loop_stop()
	client.disconnect()

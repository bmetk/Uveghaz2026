import time
import board
import busio
import json
import paho.mqtt.client as mqtt
import adafruit_bh1750

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
gy302_1 = adafruit_bh1750.BH1750(i2c, address=0x23)
gy302_2 = adafruit_bh1750.BH1750(i2c, address=0x5c)

try:
	while True:
		lux_1 = gy302_1.lux
		lux_2 = gy302_2.lux

		payload = {
			"fényerő_jobb": round(lux_1, 1),
			"fényerő_bal": round(lux_2, 1)
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

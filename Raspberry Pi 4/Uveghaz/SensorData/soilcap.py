import time
import board
import busio
import digitalio
import json
import paho.mqtt.client as mqtt
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

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
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D25)
mcp = MCP.MCP3008(spi, cs)
soilcap = AnalogIn(mcp, MCP.P0)

# Soilcap Sensor Thresholds (voltage)
dry_soil = 2
wet_soil = 1

try:
	while True:
		soil_v = soilcap.voltage

		moisture_v = (dry_soil - soil_v) / (dry_soil - wet_soil) *100
		moisture_percent = max(0, min(100, moisture_v))

		payload = {
			"talaj_fesz": round(soil_v, 3),
			"talaj_nedvesség_százalék": round(moisture_percent, 1)
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

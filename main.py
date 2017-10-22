import time
import os
import time
import RPi.GPIO as GPIO

from src import MqttLight
from ruamel.yaml import YAML

CONFIG_DIR = os.getenv('XDG_CONFIG_HOME') or os.path.expanduser('~/.config')
MQTT_CONFIG_FILE = os.path.join(CONFIG_DIR, 'mqtt.yaml')

try:
  print("Loading config: " + MQTT_CONFIG_FILE)
  config = YAML(typ='safe').load(open(MQTT_CONFIG_FILE))
  print("Connecting to mqtt")
  mqtt_light = MqttLight(config)
  while True:
    print("Berp...")
    time.sleep(1)
except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()
from mqtt_controller import MqttController
from color_controller import ColorController

import json

class MqttLight(MqttController):
  def __init__(self, config):
    MqttController.__init__(self, config)
    self.red = ColorController(17)
    self.green = ColorController(22)
    self.blue = ColorController(27)
    self.color = { 'r': 0, 'g': 0, 'b': 0 }
    self.on = False
    self.update_leds()

  def update_leds(self):
    print("Updating leds")
    if self.on:
      self.red.set(self.color['r']/255.0*100)
      self.green.set(self.color['g']/255.0*100)
      self.blue.set(self.color['b']/255.0*100)
    else:
      self.red.off()
      self.green.off()
      self.blue.off()

  def on_connect(self, client, userdata, flags, rc):
    print("Connected to home assistant broker and subscribe to: " + self.config['topic'])
    self.client.subscribe(self.config['topic']) # just grab when home assistant want to make tts

  def on_message(self, client, userdata, msg):
    print('[Got]: {}'.format(msg.payload))

    action = json.loads(msg.payload)
    state  = action['state']
    if state == 'ON':
      self.on = True
      self.color = { 'r': 255, 'g': 255, 'b': 255 }
    elif state == 'OFF':
      self.on = False
      self.color = { 'r': 0, 'g': 0, 'b': 0 }

    if action.has_key('color'):
      self.color = action['color']
    self.update_leds()
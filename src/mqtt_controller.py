import paho.mqtt.client as mqtt

class MqttController:
  def __init__(self, config):
    self.config = config
    self.client = mqtt.Client()

    self.client.on_connect = self.on_connect
    self.client.on_message = self.on_message

    self.client.username_pw_set(self.config['username'], self.config['password'])
    self.client.connect(self.config['host'], self.config['port'], 60)
    self.client.loop_start()

  def on_connect(self, client, userdata, flags, rc):
    print 'connect'
  def on_message(self, client, userdata, msg):
    print 'message'
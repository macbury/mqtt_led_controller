import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class ColorController:
  def __init__(self, pin):
    self.pin = pin
    self.power = 0
    self.pwm = None
    
  def on(self):
    if self.pwm == None:
      GPIO.setup(self.pin, GPIO.OUT)
      self.pwm = GPIO.PWM(self.pin, 100)
      self.pwm.start(100)

  def off(self):
    if self.pwm != None:
      self.pwm.stop()
    self.pwm = None
    GPIO.setup(self.pin, GPIO.IN)

  def set(self, power):
    self.on()
    self.power = 100 - power
    self.pwm.ChangeDutyCycle(self.power)
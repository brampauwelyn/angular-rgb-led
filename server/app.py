from flask import Flask, request
from gpiozero import RGBLED
from time import sleep

app = Flask(__name__)

# define the GPIO pins for the led lights

redpin = 14
greenpin = 18
bluepin = 15

led = RGBLED(redpin, greenpin, bluepin)

@app.route('/hello')
def hello():
  return "world"

@app.route('/led', methods = ['GET'])
def changeLedColor():
  red = int(request.args.get('r')) / 255
  green = int(request.args.get('g')) / 255
  blue = int(request.args.get('b')) / 255
  led.color = (red,green,blue)
  led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0, on_color=(red, green, blue), off_color=(red, green, blue), n=None, background=True)
  return "OK"
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

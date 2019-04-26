from flask import Flask, request
from gpiozero import RGBLED
from time import sleep

app = Flask(__name__)

# define the GPIO pins for the led lights


@app.route('/hello')
def hello():
  return "world"

@app.route('/led', methods = ['GET'])
def changeLedColor():
  redpin = 14
  greenpin = 18
  bluepin = 15
  led = RGBLED(redpin, greenpin, bluepin)
  red = int(request.args.get('r')) / 255
  green = int(request.args.get('g')) / 255
  blue = int(request.args.get('b')) / 255
  led.color = (red,green,blue)
  sleep(0.1)
  return "red: {}, green:  {}, blue: {}".format(red,green,blue)

  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

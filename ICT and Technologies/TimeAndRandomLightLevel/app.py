from flask import Flask
from flask import render_template
from datetime import datetime
from random import uniform

def random_light():
    light=uniform(0,1000)
    return "The light is " + str(round(light,2)) + "W/m^2."

def current_time():
    rightNow = datetime.now()
    time = rightNow.strftime("%I:%M%p")
    time = time.lstrip('0')
    time = time.lower()
    day = rightNow.strftime("%A")

    return "It is " + time + " on " + day + "."

app = Flask(__name__)

@app.route('/')
def display():
    return render_template("TimeAndLight.html",
                            time=current_time(),
                            light=random_light())

if __name__ == '__main__':
    app.run(port=5000)
from flask import Flask
from flask import render_template
from datetime import datetime
from random import uniform

def random_light():
    light=uniform(0,1000)
    output="The light is " + str(round(light,2)) + "W/m^2."

    return output

def current_time():
    rightNow = datetime.now()
    time = rightNow.strftime("%I:%M%p")
    time = time.lstrip('0')
    time = time.lower()
    day = rightNow.strftime("%A")
    output="It is " + time + " on " + day + "."

    return output

def AppendFunction(sampleList):
    sample=(current_time(),random_light())
    sampleList.append(sample)
    if len(sampleList)>10:
        return sampleList.clear()
    else:
        return sampleList

samples=[]

app = Flask(__name__)

@app.route('/')
def display():
    AppendFunction(samples)
    return render_template("index.html",
                            samples=samples)

if __name__ == '__main__':
    app.run(port=5000)
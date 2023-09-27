from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
    "https://media.giphy.com/media/d9eL06htb5Vks/giphy.gif",
    "https://media.giphy.com/media/COGHvkvkhNSqk/giphy.gif",
]
dogs_img = [
    "https://media.giphy.com/media/2C2qwckZzyiz8UzvzK/giphy.gif",
    "https://media.giphy.com/media/xT0xeuOy2Fcl9vDGiA/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

@app.route('/dogs')
def dogs():
    url = random.choice(dogs_img)
    return render_template('dogs.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

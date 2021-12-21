from flask import Flask, render_template, request
import price_pred as pp

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route("/predict", methods = ['POST'])
def predict():
    if request.method == 'POST':
        weight = request.form['weight']
        width = request.form['width']
        height = request.form['height']
        rom = request.form['rom']
        ram = request.form['ram']
        battery = request.form['battery']
        brand = request.form.get('brand')
        pr = pp.price_prediction(weight, width, height, rom, ram, battery, brand)

    return render_template("index.html", price=pr[0], rec1=pr[1], rec2=pr[2], rec3=pr[3])

if __name__ == "__main__":
    app.run(debug=True)

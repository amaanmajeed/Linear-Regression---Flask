from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Linear.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['budget']
    # data1 = request.form['my_budget']

    data1 = float(data1)
    
    print(type(data1))
    print(data1)

    arr = np.array([[data1]])
    pred = model.predict(arr)
    pred = format(pred[0], '.3f')
    return render_template("result.html", data=pred)


if __name__ == "__main__":
    app.run(debug=True)

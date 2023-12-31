# Linear Regression Web App

This is a Flask web app that loads a pre-trained linear regression model to predict a numerical value based on user input. The user enters a budget value through a form on the web page, which is then used to make a prediction using the loaded model. The predicted value is then displayed on the web page.

## Installation

1. Clone the repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the app using `python app.py`.
4. Open your web browser and navigate to `http://localhost:5000`.

## Usage

1. Enter a budget value in the input field on the home page.
2. Click the "Predict" button to make a prediction.
3. The predicted value will be displayed on the page.

## Files

- `app.py`: The main Flask application file.
- `Linear.pkl`: The pre-trained linear regression model.
- `index.html`: The HTML template for the home page.
- `requirements.txt`: The list of required Python packages.

## Credits

This app was created by Amaan Majeed. The pre-trained model was created using a sinple Linear Regression model, which was intended to predict the budget of TVs sold.
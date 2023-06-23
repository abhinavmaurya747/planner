from flask import Flask, request, render_template, jsonify
import openai
from openai_utils import get_meal_plan

openai.api_key = "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"

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        user_meals = request.form['user_meals']
        # print(user_meals)
        meal_plan = get_meal_plan(user_meals)
        # print(meal_plan)
        return jsonify({"meal_plan" : meal_plan})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
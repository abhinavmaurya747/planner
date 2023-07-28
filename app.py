from flask import Flask, request, render_template
import openai
from scheduler import *
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
async def index():
    if request.method == "POST":
        user_data = request.form
        meal_requirements = dict(user_data)
        print("User Sent : ", meal_requirements)
        sch = Schedulder(meal_requirements)
        json_data = await sch.planner()
        left_day = await sch.find_leftover_takeout()
        final_treats = await sch.find_treats()
        sch.dump()

        json_data = json_data[:-1] + "," + \
            left_day[1:-1] + "," + final_treats[1:]

        print(json_data)

        return json_data

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

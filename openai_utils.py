import openai

def get_meal_plan(user_meals, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    messages = create_message(user_meals)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message['content']

def create_message(user_meals):
    messages = [
        {'role' : 'system',
         'content' : '''You are a nutrionist whose role is to understand what your patients prefers to eat or drink.
         From the provided data you have to first find out what types of meals patient can prefer. 
         On the basis of your understanding, create a meal plan to follow as per weekly and daily schedule. 
         The consisting of various meals as per the user's need. 
         Then you have also to list all the ingredient list for those meals.
         '''},
         {'role' : 'user',
          'content' : user_meals
          }
    ]
    return messages
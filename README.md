# Meal Planner

Welcome to the Meal Planner project! This application is designed to help you create a personalized weekly meal plan based on your preferences. It utilizes the OpenAI GPT-3.5 API for natural language processing and is built using Python with Flask as the server. The frontend is created using Bootstrap, HTML, and JavaScript.

## Live Application

You can access the live version of the Meal Planner application at [https://test-djo2.onrender.com](https://test-djo2.onrender.com). Please note that the application may take some time to load, as it is hosted on a free tier and may be removed after periods of inactivity.

## Screenshots
![image](https://github.com/abhinavmaurya747/planner/assets/27424280/879a549b-51fe-455f-b931-c9138dc37866)
![image](https://github.com/abhinavmaurya747/planner/assets/27424280/2da5a676-4bd2-4137-8041-b6e642c0900c)
![image](https://github.com/abhinavmaurya747/planner/assets/27424280/1dae6af7-5ed3-435f-bbb6-6333f81577cd)
![image](https://github.com/abhinavmaurya747/planner/assets/27424280/de0cd109-83ee-4b11-93da-324096b1bb2c)
![image](https://github.com/abhinavmaurya747/planner/assets/27424280/baf85ca1-5def-49bf-8e82-c888a2c16423)

## How the Meal Planner Works

The Meal Planner will guide you through a series of questions to understand your meal preferences and dietary restrictions. Based on your answers, it will create a customized one-week meal plan for you. Here are the questions it will ask:

1. **Which meals do you want to include in your 1-week meal plan?** 
   You can choose from breakfast, lunch, dinner, morning snack, and afternoon snack. Please let us know which of these meals you would like to include in your plan.

2. **Are you vegan?** 
   Let us know if you follow a vegan diet so that we can consider plant-based options in your meal plan.

3. **Your food genre preferences:**
   Please specify any food genres you prefer, such as Mexican, Italian, Chinese, etc. This will help us tailor the meal plan to your taste.

4. **Preferred foods:**
   Add at least 5-10 specific foods that you enjoy eating. This will allow us to include your favorite dishes in the meal plan.

5. **Foods to avoid:**
   If there are any foods you want to avoid or are allergic to, kindly mention them here. We'll make sure not to include them in your meal plan.

6. **Allergic foods:**
   If you have any specific food allergies, please let us know, and we'll take this into account when planning your meals.

7. **When do you want to plan leftovers?**
   You can specify a day and mealtime when you would like to incorporate leftovers into your meal plan. For example, "Thursdays for dinner."

8. **When do you want to plan takeout food?**
   Let us know the days and mealtime when you would like to include takeout food in your meal plan. For example, "All day Saturday and Wednesday dinner."

9. **If you'd like to plan treats in your plan, what are fun foods you enjoy?**
   Mention any fun foods or treats that you enjoy. We'll include them in your meal plan to add some delight to your week.

## Running the Application Locally

If you prefer to run the Meal Planner application locally on your machine, follow these steps:

1. Clone the repository from GitHub: [https://github.com/abhinavmaurya747/planner](https://github.com/abhinavmaurya747/planner)

2. Set up a virtual environment and install the required dependencies by running:
    pip install -r requirements.txt

3. Obtain the necessary API keys for the OpenAI GPT-3.5 API and add them to the project's configuration.

4. Run the Flask server by executing the following command in the project's root directory:
    python app.py

5. Access the application locally by navigating to `http://localhost:5000` in your web browser.

## Contributing

We welcome contributions to improve the Meal Planner application. If you find any issues or have ideas for enhancements, please feel free to open a pull request or submit an issue on the GitHub repository.

Thank you for using the Meal Planner application! We hope it helps you create a delicious and personalized meal plan for the week. If you have any questions or feedback, please don't hesitate to reach out to us. Happy meal planning!

// Function to handle form submission
function handleSubmit(event) {
  event.preventDefault(); // Prevent the default form submission

  // Get the form data
  const form = event.target;
  const formData = new FormData(form);

  // Send the POST request
  fetch(form.action, {
    method: form.method,
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      const mealPlan = data.meal_plan.replace(/\\n/g, "\n");
      // Update the value of the meal_plan textarea
      const mealPlanTextarea = document.getElementById("meal_plan");
      mealPlanTextarea.style.display = "block";
      mealPlanTextarea.value = mealPlan;
      const lineCount = mealPlan.split("\n").length;
      mealPlanTextarea.rows = lineCount;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Add event listener to the form submit event
const form = document.querySelector("form");
form.addEventListener("submit", handleSubmit);

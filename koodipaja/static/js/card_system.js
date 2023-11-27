document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM content loaded");
  fetchData();
});

async function fetchData() {
  try {
    console.log("Fetching data...");
    const response = await fetch("/get_data/");
    const data = await response.json();

    console.log("Data received:", data);
    updateHTML(data);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

function updateHTML(data) {
  console.log("Updating HTML with data:", data);
  const dataContainer = document.getElementById("data-container");

  const listItems = data.map(
    (pair) => `<li>${pair.question}: ${pair.answer}</li>`
  );
  dataContainer.innerHTML = `<ul>${listItems.join("")}</ul>`;
}

// Function to fetch data from the Django API
// async function fetchData() {
//   try {
//     const response = await fetch("/api/questions"); // Replace with your actual API endpoint
//     const data = await response.json();
//     return data;
//   } catch (error) {
//     console.error("Error fetching data:", error);
//     return [];
//   }
// }

// // Function to handle card click event
// async function handleCardClick() {
//   const cardContent = document.getElementById("cardContent");

//   // Fetch data from the API
//   const questionAnswerPairs = await fetchData();

//   // Check if there is data available
//   if (questionAnswerPairs.length > 0) {
//     // Display the question for the current card
//     cardContent.textContent = `Question: ${questionAnswerPairs[0].question}`;

//     // Rotate the question-answer pairs for the next click
//     questionAnswerPairs.push(questionAnswerPairs.shift());
//   } else {
//     // Handle the case where no data is available
//     cardContent.textContent = "No questions available.";
//   }
// }

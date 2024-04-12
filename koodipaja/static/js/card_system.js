    // The fetch() function initiates an asynchronous network request to retrieve data from the specified URL.
    // I'm using a Django REST Framework to make the api route.
    fetch("/api/question_answer/")
      // The first .then() method is used to handle the response once it’s available. It ensures that we don’t block the main thread while waiting for the data.
      // Without this step, we’d have the raw response, which includes headers, status codes, and other metadata.
      .then(response => response.json())
      // This chaining ensures that each step happens in order, even though they’re asynchronous.
      .then(questions_and_answers => {

        // There's a question and answer key-value pair in the data, track both indeces separately, starting from 0
        let questionIndex = 0;
        let answerIndex = 0;

        // The id of the element where the question and answer should go (it's in the html file)
        const myTextElement = document.getElementById('myText');
        // Button id
        const changeButton = document.getElementById('changeButton');

        // Event listener that triggers when 'changeButton' is clicked
        changeButton.addEventListener('click', () => {
          console.log(questions_and_answers);
          // If questionIndex is greater than answerIndex it means the text ('myText') should be
          // answer_text next. Also check that the indeces aren't greater than the length of the
          // array.
          if (questionIndex > answerIndex && questionIndex <= questions_and_answers.length) {
            // First answerIndex is 0.
            // answer_text is comes from the model (in models.py)
            myTextElement.textContent = questions_and_answers[answerIndex].answer_text;
            // Next time check the next index by incrementing the index by 1
            answerIndex++;
          }
          // If the indeces are equal then the next text should be a question_text, since I want to
          // alternate between questions and answers.
          // If the if statement's condition is true then all questions and answers have been
          // cycled through and code continues in the else block.
          else if (questionIndex === answerIndex && questionIndex <= (questions_and_answers.length - 1)) {
            myTextElement.textContent = questions_and_answers[questionIndex].question_text;
            questionIndex = questionIndex + 1;
          }
          else {
            myTextElement.textContent = "Out of questions and answers!";
            // TODO: Start again option?
          }
        });
      })
      .catch(error => console.error('Error fetching data:', error));












// Some old code I've banged my head against the wall with

// document.addEventListener("DOMContentLoaded", function () {
//   console.log("DOM content loaded");
//   fetchData();
// });

// async function fetchData() {
//   try {
//     console.log("Fetching data...");
//     const response = await fetch("/api/question_answer/");
//     const data = await response.json();

//     console.log("Data received:", data);
//     // updateHTML(data);
//     handleCardClick(data);
//     clicked = false;
//     return data;
//   } catch (error) {
//     console.error("Error fetching data:", error);
//   }
// }

// function updateHTML(data) {
//   console.log("Updating HTML with data:", data);
//   const dataContainer = document.getElementById("data-container");

//   // question_text and answer_text are from the model QuestionAnswerPair
//   const listItems = data.map(
//     (pair) => `<ol>${pair.question_text + " " + pair.answer_text}</ol>`
//   );

//   for (let i = 0; i < listItems.length; i++){
//     dataContainer.innerHTML += `<ul>${listItems[i]}</ul>`;
// }
// }

// Function to fetch data from the Django API
// async function fetchData() {
//   try {
//     const response = await fetch("/api/question_answer"); // Replace with your actual API endpoint
//     const data = await response.json();
//     console.log(data);
//     return data;
//   } catch (error) {
//     console.error("Error fetching data:", error);
//     return [];
//   }
// }

// Function to see if element has been clicked
// var elementId = 'question';
// let elementClicked = false;
// var questionContainer = document.getElementById(elementId);
// questions_and_answers = [];
// questionContainer.addEventListener('click', function() {
//   console.log("Element clicked!");
//   elementClicked = true;
// })

// // Function to handle card click event
// function handleCardClick(data, clicked) {
//   var answerContainer = document.getElementById("answer");
  // const dictionary = Object.fromEntries(data.map(({question_text, answer_text}) => [
  //   question_text, answer_text]));
  // if (!clicked){
  //   for (i = 0; i < data.length; i++){
  //     questions_and_answers.push((data[i].question_text));
  //     questions_and_answers.push((data[i].answer_text));
  //   }
  //   clicked = true;
  // }
  //   console.log("Questions and Answers: ", questions_and_answers);
    // questions_and_answers.shift();  
      // if (questionContainer.id === 'question') {
      //   questionContainer.innerHTML = questions_and_answers[0];
      // }
      // if (elementClicked === true) {
      //   questions_and_answers.shift();
      //   questionContainer.innerHTML = questions_and_answers[0];
      // }
        // if (questionContainer.id === 'answer') {
        //    {
        //     console.log("DingDingDing!");
        //   }
    // else {
    //     console.log("Wtf dood")
    // }
    // console.log(data.length);
    // console.log(data[0].question_text, data[0].answer_text);
    // }


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
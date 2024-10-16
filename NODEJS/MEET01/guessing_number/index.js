const inquirer = require("inquirer");

const min = 0;
const max = 100;
const numberToGuess = Math.floor(Math.random() * (max - min + 1)) + min;
const maxAttempts = 10;

console.log("Welcome to the Number Guessing Game!");

const playGame = (playerName, numberToGuess, attemptsLeft) => {
  if (attemptsLeft === 0) {
    console.log(
      `Sorry ${playerName}, you've run out of attempts! The number was ${numberToGuess}.`
    );
    return;
  }

  inquirer
    .prompt([
      {
        type: "input",
        name: "guess",
        message: `Guess a number between ${min} and ${max} (Attempts left: ${attemptsLeft}): `,
      },
    ])
    .then((answers) => {
      const guess = parseInt(answers.guess);
      if (guess === numberToGuess) {
        console.log(
          `Congratulations ${playerName}, you've guessed the number!`
        );
      } else {
        if (guess < numberToGuess) {
          console.log("Too Low!");
        } else {
          console.log("Too High!");
        }
        playGame(playerName, numberToGuess, attemptsLeft - 1);
      }
    });
};

inquirer
  .prompt([
    {
      type: "input",
      name: "playerName",
      message: "What is your name?",
    },
  ])
  .then((answers) => {
    const playerName = answers.playerName;
    console.log(`Hello ${playerName}! Let's start the game.`);
    playGame(playerName, numberToGuess, maxAttempts);
  });

const inquirer = require("inquirer");

const question = [
  {
    type: "input",
    name: "name",
    message: "What is your name?",
    default: "Budi",
  },
  {
    type: "list",
    name: "list_question",
    message: "Which programming language do you like?",
    choices: ["JavaScript", "Python", "Java", "C++"],
    default: "JavaScript",
  },
  {
    type: "checkbox",
    name: "checkbox_question",
    message: "Which programming language do you like?",
    choices: ["JavaScript", "Python", "Java", "C++"],
    default: "JavaScript",
  },
];

inquirer.prompt(question).then((answers) => {
  console.log(answers);
});

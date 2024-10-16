const readline = require("node:readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let A;
let B;
let C;

rl.question("Enter the length of the retangle: "),
  (answerA) => {
    A = parseFloat(answerA);
    rl.question("Enter the width of the rectangle: "),
      (answerB) => {
        B = parseFloat(answerC);
        rl.question("Enter the width of the rectangle: "),
            (answerC) => {
            C = parseFloat(answerC);
            }
            
        const D = (B ** 2) - (4 * A * C);
        const X1 = ((-B) + Math.sqrt(D)) / (2 * A);
        const X2 = ((-B) - Math.sqrt(D)) / (2 * A);
        console.log(`X: ${X1}`);
        console.log(`X: ${X2}`);
        rl.close();
      };
};

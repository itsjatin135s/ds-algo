const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const questions = ["Name ? ", "Place ? ", "Thing ? "];

const collectAnswers = (questions, done) => {
  const answers = [];

  const questionAnswered = (answer) => {
    answers.push(answer.trim());
    if (answers.length < questions.length) {
      rl.question(questions[answers.length], questionAnswered);
    } else {
      return done(answers);
    }
  };
  rl.question(questions[0], questionAnswered);
};

collectAnswers(questions, (answers) => {
  console.log("Thanks");
  console.log(answers);
  process.exit();
});

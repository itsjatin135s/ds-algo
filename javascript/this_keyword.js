let user = {
  username: "jatin",
  greet: function () {
    console.log(`welcome : ${this.username}`);
  },
};

user.greet(); // print welcome jatin

let user2 = {
  username: "jatin",
  greet: () => {
    console.log(`welcome : ${this.username}`);
  },
};

user2.greet(); // print welcome undefined

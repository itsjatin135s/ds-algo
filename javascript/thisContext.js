const person = {
    name: "Jatin",
    greet(){
        console.log(`hello ${this.name}`)
    }
}

const newGreet = person.greet;
newGreet();

const bindGreet = person.greet.bind({name:"Mr J."})
bindGreet();
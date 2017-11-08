'use strict'

const actions = ["eat", "sleep", "make_sound", "play"];
const foods = ["meat", "fish", "bugs", "grain"];

class Animal {
    constructor(energy){
        this.constructor.population++;
        this.energy = energy;
    }

    static get population() {
        return !this._population ? 0 : this._population;
    }

    static set population(pop) {
        this._population = pop;
    }

    set population(population) {}
    get population() {return Animal.population;}

    make_sound(){
        this.energy -= 3;
        console.log("My energy is :" + this.energy);
    }

    eat(){
        this.energy += 5;
    }

    sleep(food_type){
        this.energy += 10;
    }

    play(){}
}

class Jungle {
    constructor(animals=[]){
        this.animals = animals;
        this.foods = ["meat", "fish", "bugs", "grain"];
    }
    sound_off(){
        for(let animal in this.animals){
            animal.make_sound();
        }
    }
}

class Tiger extends Animal {
    constructor(energy){
        super(energy);
        this.unable_to_eat = "grains";
    }

    sleep(){
        this.energy += 5;
    }

    eat(food){
        if(food !== this.unable_to_eat){
            super.eat(food);
            return;
        }
        console.log("tiger doesnt like " + food);
    }

    make_sound() {
        super.make_sound();
        console.log("I am a tiger, roar!");
    }
}

class Monkey extends Animal {
    eat(food_type){
        this.energy += 2;
    }

    play(){
        if(this.energy > 7){
            console.log("Oooo Oooo Oooo");
            this.energy -= 8;
            return;
        }
        console.log("Monkey is too tired.");
    }

    make_sound(){
        super.make_sound();
        this.energy -= 1;
        console.log("I am a monkey, ooo-AAA!");
    }
}

class Snake extends Animal {

    make_sound(){
        super.make_sound();
        console.log("I am a snake, hisss.");
    }
}

function get_random_food(){
    return foods[Math.floor(Math.random()*foods.length)];
}

const species = [Tiger, Snake, Monkey];

var jungle = new Jungle();

for(var i=0; i<10; i++){
    let animal = species[Math.floor(Math.random()*species.length)];
    // create animal with 50 energy
    animal = new animal(Math.floor(Math.random()*50));
    jungle.animals.push(animal);
}

// test case for random animals with random actions
for(var i=0; i<jungle.animals.length;i++){
    let action = actions[Math.floor(Math.random()*actions.length)];
    let arg;
    if (action === actions[0]){
        arg = get_random_food();
    }
    jungle.animals[i][action](arg);
}


console.log("complete animal population: " + jungle.animals.length);
// is 10
console.log("Tiger population: " + Tiger.population);
console.log("Snake population: " + Snake.population);
console.log("Monkey population: " + Monkey.population);
// sums up to 10

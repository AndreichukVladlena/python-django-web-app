// Базовый класс Animal
function Animal(name, age) {
    this.name = name;
    this.age = age;
}

// Функции для базового класса Animal
Animal.prototype.introduce = function() {
    return `Hello, I'm ${this.name}!`;
};

Animal.prototype.getAge = function() {
    return this.age;
};

Animal.prototype.makeSound = function() {
    return 'Some generic animal sound.';
};

// Наследник Mammal
function Mammal(name, age, type) {
    // Вызываем конструктор родительского класса
    Animal.call(this, name, age);
    this.type = type;
}

// Прототипное наследование
Mammal.prototype = Object.create(Animal.prototype);

// Функции для наследника Mammal
Mammal.prototype.sound = function() {
    return 'Mammals make various sounds.';
};

Mammal.prototype.feedMilk = function() {
    return 'Mammals feed their young with milk.';
};

// Наследник Lion
function Lion(name, age, type, roarPower) {
    // Вызываем конструктор родительского класса
    Mammal.call(this, name, age, type);
    this.roarPower = roarPower;
}

// Прототипное наследование
Lion.prototype = Object.create(Mammal.prototype);

// Декоратор для функции sound у класса Mammal
function soundDecorator(originalFunction) {
    return function() {
        const originalResult = originalFunction.call(this);
        return `${originalResult} Lions roar loudly!`;
    };
}

// Применяем декоратор к функции sound
Mammal.prototype.sound = soundDecorator(Mammal.prototype.sound);

// Функции для наследника Lion
Lion.prototype.roar = function() {
    return `Roar! This lion's roar power is ${this.roarPower}.`;
};

Lion.prototype.hunt = function() {
    return 'Lions are skilled hunters.';
};

// Пример использования классов и декоратора
const lion = new Lion('Leo', 5, 'Predator', 'Strong');
console.log(lion.introduce()); // Output: Hello, I'm Leo!
console.log(lion.getAge()); // Output: 5
console.log(lion.sound()); // Output: Mammals make various sounds. Lions roar loudly!
console.log(lion.roar()); // Output: Roar! This lion's roar power is Strong.
console.log(lion.hunt()); // Output: Lions are skilled hunters.

document.querySelector('#introduce-button').addEventListener('click', ()=>{
   document.querySelector('#proto-result-text').textContent += `${lion.introduce()} `;
   document.querySelector('#introduce-button').disabled = true;
});

document.querySelector('#age-button').addEventListener('click', ()=>{
   document.querySelector('#proto-result-text').innerHTML += `${lion.getAge()} `;
   document.querySelector('#age-button').disabled = true;
});

document.querySelector('#sound-button').addEventListener('click', ()=>{
   document.querySelector('#proto-result-text').innerHTML += `${lion.sound()} `;
   document.querySelector('#sound-button').disabled = true;
});

document.querySelector('#roar-button').addEventListener('click', ()=>{
   document.querySelector('#proto-result-text').innerHTML += `${lion.roar()} `;
   document.querySelector('#roar-button').disabled = true;
});

document.querySelector('#hunt-button').addEventListener('click', ()=>{
   document.querySelector('#proto-result-text').innerHTML += `${lion.hunt()}\n`;
   document.querySelector('#hunt-button').disabled = true;
});

// Базовый класс Worker
class ZooWorker {
    constructor(name, age, salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    // Геттер для имени
    getName() {
        return this.name;
    }

    // Сеттер для возраста
    setAge(newAge) {
        this.age = newAge;
    }

    // Обычная функция базового класса
    greet() {
        return `Hello, I'm ${this.name}, a zoo worker.`;
    }

    // Декоратор для функции greet
    static greetDecorator(originalFunction) {
        return function() {
            const originalResult = originalFunction.call(this);
            return `${originalResult} Welcome to the zoo!`;
        };
    }

    // Применяем декоратор к функции greet
    greet = ZooWorker.greetDecorator(this.greet);
}

// Наследник ZooAnimalHandler
class AnimalHandler extends ZooWorker {
    constructor(name, age, salary, specialty) {
        super(name, age, salary);
        this.specialty = specialty;
    }

    // Геттер для специальности
    getSpecialty() {
        return this.specialty;
    }

    // Дополнительная функция для наследника
    handleAnimal(animal) {
        return `${this.name} is handling ${animal}.`;
    }
}

// Наследник ZooTrainer
class Trainer extends AnimalHandler {
    constructor(name, age, salary, specialty, trainingMethod) {
        super(name, age, salary, specialty);
        this.trainingMethod = trainingMethod;
    }

    // Геттер для метода обучения
    getTrainingMethod() {
        return this.trainingMethod;
    }

    // Дополнительная функция для наследника
    trainAnimal(animal) {
        return `${this.name} is training ${animal} using ${this.trainingMethod}.`;
    }
}

// Пример использования классов и декоратора
const zooWorker = new ZooWorker('John', 30, 40000);
console.log(zooWorker.greet()); // Output: Hello, I'm John, a zoo worker. Welcome to the zoo!

const animalHandler = new AnimalHandler('Alice', 25, 35000, 'Mammals');
console.log(animalHandler.handleAnimal('lion')); // Output: Alice is handling lion.

const trainer = new Trainer('Bob', 35, 50000, 'Birds', 'Positive Reinforcement');
console.log(trainer.trainAnimal('parrot')); // Output: Bob is training parrot using Positive Reinforcement.

document.querySelector('#worker-info-button').addEventListener('click', () => {
     document.querySelector('#extends-result-text').innerHTML += `Name: ${trainer.name}, age: ${trainer.age}, salary: ${trainer.salary}, speciality: ${trainer.specialty} `;
     document.querySelector('#worker-info-button').disabled = true;
});

document.querySelector('#training-meth-button').addEventListener('click', () => {
     document.querySelector('#extends-result-text').innerHTML += `${trainer.trainingMethod} `;
     document.querySelector('#training-meth-button').disabled = true;
});

document.querySelector('#train-animal-button').addEventListener('click', () => {
     document.querySelector('#extends-result-text').innerHTML += `${trainer.trainAnimal('parrot')} `;
     document.querySelector('#train-animal-button').disabled = true;
});


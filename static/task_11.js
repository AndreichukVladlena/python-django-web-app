"use strict";

 // Ассоциативный массив для хранения данных об автомобилях
const cars = [];
 function addCar() {
            // Получаем значения из формы
     const carBrand = document.getElementById('carBrand').value;
     const carNumber = document.getElementById('carNumber').value;
     const ownerName = document.getElementById('ownerName').value;

     // Добавляем данные в массив
     cars.push({
         brand: carBrand,
         number: carNumber,
         owner: ownerName,
     });
     // Очищаем форму
     document.getElementById('carForm').reset();
 }

 function searchCars() {
     // Получаем значение для поиска
     const searchBrand = document.getElementById('searchBrand').value;

     // Ищем автомобили с заданной маркой
     const resultCars = cars.filter(car => car.brand === searchBrand);

     // Отображаем результат
     displayResult(resultCars);
 }

 function displayResult(cars) {
     const resultDiv = document.getElementById('result');
     resultDiv.innerHTML = ''; // Очищаем предыдущий результат
      if (cars.length === 0) {
          resultDiv.textContent = 'Автомобилей с указанной маркой не найдено.';
      } else {
          const resultList = document.createElement('ul');
          cars.forEach(car => {
              const listItem = document.createElement('li');
              listItem.textContent = `Фамилия владельца: ${car.owner}, Номер автомобиля: ${car.number}`;
              resultList.appendChild(listItem);
          });
          resultDiv.appendChild(resultList);
      }
 }

 document.querySelector('#add-car').addEventListener('click', () => {
     addCar();
 });

 document.querySelector('#find-car').addEventListener('click', () => {
     searchCars();
 });


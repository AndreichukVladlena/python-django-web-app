"use strict";

function calculateResult(){
    let totalAmount = 0;

    let food_cons = document.querySelectorAll('#amount');
    food_cons.forEach((item) => {
        totalAmount+= parseInt(item.innerHTML);
        console.log(item.innerHTML + " " + totalAmount);
    });

    return totalAmount;
}

 document.querySelector('#sum-food').addEventListener('click', () => {
        // Предотвратить стандартное поведение формы (перезагрузку страницы)
     let res = document.createElement('p');
     res.innerHTML = "Суммарное кол-во еды, съеденное животным: " + calculateResult();
     document.querySelector('#result-sum').append(res);
     document.querySelector('#sum-food').disabled = true;
 });
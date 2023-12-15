"use strict";

document.querySelector('.icon').addEventListener('click', function() {
    document.querySelector('.side-menu').classList.toggle('show');
});
    document.querySelector('.hide-menu').addEventListener('click', function() {
    document.querySelector('.side-menu').classList.toggle('show');
});

    //is user older than 18

    let days = ['воскресенье', 'понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу'];

    if (!localStorage.getItem('isNewUser')){
        let birthDate = new Date(prompt('Введите даты рождения. (YYYY-MM-DD)', '100'));
        let age = new Date(Date.now() - birthDate);
        age = age.getFullYear() - 1970;

        if (+age < 18){
            alert('Политика нашего сайта не рекомендует его к использованию лицам не достигшим 18 лет!');
        }

        alert(`Вы родились в ${days[birthDate.getDay()]}!`);

    }

    //timer

    let timerElement = document.querySelector('.timer');

    let counter = sessionStorage.getItem('timer') ?? 0;

    function timer(element = timerElement){
        if(counter == 3600){
            counter = 0;
        }

        element.innerHTML = `${Math.floor(counter/60)} : ${counter%60}`;
        counter++;
    }

    setInterval(timer, 1000);
    window.addEventListener('beforeunload', () => sessionStorage.setItem('timer', counter));

    //variable to save info about user session

    let isNewUser = localStorage.setItem('isNewUser', false);

    //edit form's style

    let styleEditElement = document.querySelector('#edit-style');
    let editFormStyle = document.querySelector('.edit-form-style');

    //add checkbox for increase font-size

    let increaseFontSize = document.createElement('input');
    let increaseFontSizeLabel = document.createElement('label');

    increaseFontSize.type = "checkbox";
    increaseFontSize.id = "increase-font-size-checkbox";

    increaseFontSizeLabel.innerHTML = "Увеличить размер шрифта";
    increaseFontSizeLabel.for = "increase-font-size-checkbox";

    //add checkbox for decrease font-size

    let decreaseFontSize = document.createElement('input');
    let decreaseFontSizeLabel = document.createElement('label');

    decreaseFontSize.type = "checkbox";
    decreaseFontSize.id = "decrease-font-size-checkbox";

    decreaseFontSizeLabel.innerHTML = "Уменьшить размер шрифта";
    decreaseFontSizeLabel.for = "decrease-font-size-checkbox";

    //add checkbox for change text color

    let editTextColor = document.createElement('input');
    let editTextColorLabel = document.createElement('label');

    editTextColor.type = "checkbox";
    editTextColor.id = "edit-text-color-checkbox";

    editTextColorLabel.innerHTML = "Изменить цвет шрифта";
    editTextColorLabel.for = "edit-text-color-checkbox";

    //add checkbox for change bg color

    let editBGColor = document.createElement('input');
    let editBGColorLabel = document.createElement('label');

    editBGColor.type = "checkbox";
    editBGColorLabel.id = "edit-bg-color-checkbox";

    editBGColorLabel.innerHTML = "Изменить цвет фона";
    editBGColorLabel.for = "edit-bg-color-checkbox";

    styleEditElement.addEventListener('click', () => {
     editFormStyle.append(increaseFontSize);
     editFormStyle.append(increaseFontSizeLabel);

     editFormStyle.append(decreaseFontSize);
     editFormStyle.append(decreaseFontSizeLabel);

     editFormStyle.append(editTextColor);
     editFormStyle.append(editTextColorLabel);

     editFormStyle.append(editBGColor);
     editFormStyle.append(editBGColorLabel);
    });

styleEditElement.addEventListener('dblclick', ()=>{
     increaseFontSize.remove();
     increaseFontSizeLabel.remove();

     decreaseFontSize.remove();
     decreaseFontSizeLabel.remove();

     editTextColor.remove();
     editTextColorLabel.remove();

     editBGColor.remove();
     editBGColorLabel.remove();
});

editBGColor.addEventListener('change', () => {
    document.querySelector('.js-page').classList.toggle('change-bg');
});

increaseFontSize.addEventListener('change', () => {
    document.querySelector('.js-page').classList.toggle('increase-font-size');
});

decreaseFontSize.addEventListener('change', () => {
    document.querySelector('.js-page').classList.toggle('decrease-font-size');
});

editTextColor.addEventListener('change', () => {
    document.querySelector('.js-page').classList.toggle('edit-text-color');
});


//focus blur

//ad rotation

let imgSources = ['static/7karat.jpg', 'static/mila.jpg', 'static/wb.png'];
let adLinks = ['https://7karat.by/', 'https://mila.by/', 'https://www.wildberries.ru/'];
let flag=true;
let startStopButton = document.querySelector('#start-stop');

startStopButton.addEventListener('click', ()=>{

    if(flag){

        startStopButton.value="Cтоп";
        imageRotation();
        flag=false;

    }else{

        startStopButton.value="Старт";
        imageRotation(0, false);
        flag=true;

    }
});

window.addEventListener('blur', () => {
   imageRotation(0, false);
   startStopButton.value="Старт";
    flag=true;
});

window.addEventListener('scroll', ()=>{
    let documentHeight = document.documentElement.scrollHeight;
    let documentScrolled = document.documentElement.scrollTop;
    let scrolledPercentage = (documentScrolled / documentHeight) * 100;
    document.getElementById("monkey").style.left = scrolledPercentage.toString() + "%";
    document.getElementById("banana").style.right = scrolledPercentage.toString() + "%";
    console.log(document.documentElement.scrollHeight);
});

document.querySelector('#add-row-button').addEventListener('click', ()=>{
     addRow(document.querySelector('#table-test-js'));
});

document.querySelector('#add-column-button').addEventListener('click', ()=>{
     addColumn(document.querySelector('#table-test-js'));
});

document.querySelector('#transpose-button').addEventListener('click', ()=>{
     transposeTable(document.querySelector('#table-test-js'));
});

//table

let tableTDlist;
let tableTDAmount = document.querySelector('#el-amount');

tableTDAmount.addEventListener('change', ()=>{
    let tableContainer = document.querySelector('.table-range');

    if(document.querySelector('#table-test-js')){
        document.querySelector('#table-test-js').remove();
    }else{
        document.querySelector('#add-row-button').disabled=false;
        document.querySelector('#add-column-button').disabled=false;
        document.querySelector('#transpose-button').disabled=false;
        document.querySelector('#select-limit').disabled=false;
    }

    tableContainer.append(createTable(tableTDAmount.value));

    tableTDlist = document.querySelectorAll("#td-table-test-js");

    tableTDlist.forEach((td) => createTableTdEvent(td));

});

function createTable(cellAmount){

    let tableElement= document.createElement('table');
    tableElement.id="table-test-js";
    tableElement.style["padding"]="60px";
    tableElement.classList.add ("center");

    let tableTD, tableTR;

    for(let i=0; i < cellAmount; i++){
        if (i%5 == 0 || i==0){

            tableTR = tableElement.insertRow();

        }

        tableTD = tableTR.insertCell();
        tableTD.id = "td-table-test-js";
        tableTD.innerHTML = String(getRandomInt(50));

    }

    return tableElement;

}

//table td func

function createTableTdEvent(td){

    td.addEventListener('click', () => {
        if(!td.classList.contains('disabled-td') && selectCell(td, +document.querySelector('#select-limit').value)){

             if (td.innerHTML%2==0) {
                 td.style["background"]="pink";
            } else {
                td.style["background"]="#e4e6c9ff";
            }
             td.classList.add('selected-cell');
             td.nextSibling.classList.add('disabled-td');
             td.previousSibling.classList.add('disabled-td');
             selectCell(td, 3);
        }

    });

}

//random func

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

let timeOut;
function imageRotation(i= 0, flag=true) {
    if(!flag){
        clearTimeout(timeOut);
        return false;
    }
    let image = document.getElementById("rotator");
    let link = document.getElementById("ad-link");
    image.src = imgSources[i];
    link.href= adLinks[i];
    i++;
    if (i == imgSources.length) i = 0;

    timeOut = setTimeout(`imageRotation(${i})`, document.querySelector('#delay').value);
}

function addRow (table) {
        let newRow = table.insertRow();
        for (let i = 0; i < 5; i++) {
            let newCell = newRow.insertCell();
            newCell.id = "td-table-test-js";
            newCell.innerHTML = String(getRandomInt(50));
            createTableTdEvent(newCell);
        }
        return table;
}

 function addColumn (table) {
        let rows = table.rows;

        for (let i = 0; i < rows.length; i++) {
            let newCell = rows[i].insertCell();

            let prev = newCell.previousSibling;
            if (prev.classList.contains('selected-cell')) newCell.classList.add('disabled-td');

            newCell.id = "td-table-test-js";
            newCell.innerHTML = String(getRandomInt(50));
            createTableTdEvent(newCell);
        }

    return table;
}

function transposeTable (table) {
    let rows = table.rows;
    let cols = rows[0].cells.length;

    //new table
    let transposedTable = document.createElement('table');
    transposedTable.id = "table-test-js";
    transposedTable.style["padding"] = "60px";
    transposedTable.classList.add("center");

    //tds of new table
    for (let j = 0; j < cols; j++) {
        let newRow = transposedTable.insertRow();
        for (let i = 0; i < rows.length; i++) {
            let newCell = newRow.insertCell();
            newCell.id = "td-table-test-js";
            newCell.innerHTML = rows[i].cells[j].innerHTML;
            newCell.classList = rows[i].cells[j].classList;
            newCell.style.cssText = rows[i].cells[j].style.cssText;
            createTableTdEvent(newCell);
        }
    }

    table.parentNode.replaceChild(transposedTable, table);
}

function selectCell(cell, maxSelection) {
    console.log(cell.parentElement);
     let cellsSelectedInCurrRow = cell.parentElement.querySelectorAll('.selected-cell');

     return cellsSelectedInCurrRow.length >= maxSelection? false : true;
}
"use strict";

document.querySelector('.icon').addEventListener('click', function() {
    document.querySelector('.side-menu').classList.toggle('show');
});
    document.querySelector('.hide-menu').addEventListener('click', function() {
    document.querySelector('.side-menu').classList.toggle('show');
});


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

    document.addEventListener('beforeunload', () => sessionStorage.setItem('timer', counter));

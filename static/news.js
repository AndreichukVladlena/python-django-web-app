const walk = {x: 50, y: 30};

let cards = document.querySelectorAll('.news');

console.log(cards);
cards.forEach((card) => {
    card.addEventListener('mousemove', (event) => {
        const width = card.offsetWidth,
        height = card.offsetHeight;

        const xWalk = Math.round((event.x / width / 2 * walk.x) - (walk.x / 2)),
        yWalk = Math.round((event.y / height / 2  * walk.y) - (walk.y / 2));

  card.style.transform = `rotateY(${-xWalk}deg) rotateX(${yWalk}deg)`;
    });
});

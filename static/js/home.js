// //step 1: get DOM
// let nextDom = document.getElementById('next');
// let prevDom = document.getElementById('prev');

// let carouselDom = document.querySelector('.carousel');
// let SliderDom = carouselDom.querySelector('.carousel .list');
// let thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
// let thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');
// let timeDom = document.querySelector('.carousel .time');

// thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
// let timeRunning = 3000;
// let timeAutoNext = 7000;

// nextDom.onclick = function(){
//     showSlider('next');    
// }

// prevDom.onclick = function(){
//     showSlider('prev');    
// }
// let runTimeOut;
// let runNextAuto = setTimeout(() => {
//     next.click();
// }, timeAutoNext)
// function showSlider(type){
//     let  SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
//     let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
//     if(type === 'next'){
//         SliderDom.appendChild(SliderItemsDom[0]);
//         thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
//         carouselDom.classList.add('next');
//     }else{
//         SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
//         thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
//         carouselDom.classList.add('prev');
//     }
//     clearTimeout(runTimeOut);
//     runTimeOut = setTimeout(() => {
//         carouselDom.classList.remove('next');
//         carouselDom.classList.remove('prev');
//     }, timeRunning);

//     clearTimeout(runNextAuto);
//     runNextAuto = setTimeout(() => {
//         next.click();
//     }, timeAutoNext)
// }


// const sectionParallax = document.querySelector('.section-parallax');
// const sectionParallaxBackground = sectionParallax.querySelector('.background');
// const carousel = document.querySelector('.carousel');
// const carouselHeight = carousel.offsetHeight;

// const tl = gsap.timeline({ paused: true });

// tl.from(sectionParallaxBackground, { y: 500, duration: 2 })
//   .to(sectionParallaxBackground, { y: -500, duration: 20, ease: 'none' });

//   const updateParallax = () => {
//     const scrollY = window.scrollY;
//     const maxScroll = document.body.scrollHeight - window.innerHeight;
//     const scrollPercent = scrollY / maxScroll;
//     const yPos = -(carouselHeight - sectionParallax.offsetHeight) * scrollPercent;
//     sectionParallax.style.top = { yPos };px;
//     tl.progress(scrollPercent).pause();
//   };
// window.addEventListener('scroll', updateParallax);

// tl.play();

// const cards = document.querySelectorAll('.card');
// let selectedCard = null;

// function selectCard(event, card) {
  // Remove the "selected" class from all cards
  

  // Add the "selected" class to the clicked card
  // card.classList.add('selected');
  // selectedCard = card;

  // Move all cards to the left
  // cards.forEach(c => {
  //   c.style.transform = 'translateX(-100%)';
  // });

  // Bring the selected card to the front
//   const main = document.querySelector('.main');
//   main.appendChild(selectedCard);
// }

// Add initial positioning for the cards
// cards.forEach(c => {
//   c.style.transition = 'transform 0.3s ease-out';
//   c.style.transform = 'translateX(0)';
// });

//step 1: get DOM
const nextDom = document.getElementById('next');
const prevDom = document.getElementById('prev');

const carouselDom = document.querySelector('.carousel');
const SliderDom = carouselDom.querySelector('.carousel .list');
const thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
const thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');
const timeDom = document.querySelector('.carousel .time');

thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
const timeRunning = 3000;
const timeAutoNext = 7000;

nextDom.onclick = function() {
  showSlider('next');
};

prevDom.onclick = function() {
  showSlider('prev');
};

let runTimeOut;
let runNextAuto = setTimeout(() => {
  nextDom.click();
}, timeAutoNext);

function showSlider(type) {
  // Use the SliderItemsDom variable that was declared outside the function
  const SliderItemsDom = document.querySelectorAll('.carousel .list .item');
  const thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');

  if (type === 'next') {
    SliderDom.appendChild(SliderItemsDom[0]);
    thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
    carouselDom.classList.add('next');
  } else {
    SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
    thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
    carouselDom.classList.add('prev');
  }

  clearTimeout(runTimeOut);
  runTimeOut = setTimeout(() => {
    carouselDom.classList.remove('next');
    carouselDom.classList.remove('prev');
  }, timeRunning);

  clearTimeout(runNextAuto);
  runNextAuto = setTimeout(() => {
    nextDom.click();
  }, timeAutoNext);
}

const sectionParallax = document.querySelector('.section-parallax');
const sectionParallaxBackground = sectionParallax.querySelector('.background');
const carousel = document.querySelector('.carousel');
const carouselHeight = carousel.offsetHeight;

const tl = gsap.timeline({ paused: true });

tl.from(sectionParallaxBackground, { y: 500, duration: 2 })
  .to(sectionParallaxBackground, { y: -500, duration: 20, ease: 'none' });

const updateParallax = () => {
  const scrollY = window.scrollY;
  const maxScroll = document.body.scrollHeight - window.innerHeight;
  const scrollPercent = scrollY / maxScroll;
  const yPos = -(carouselHeight - sectionParallax.offsetHeight) * scrollPercent;
  sectionParallax.style.top = `${yPos}px`;
  tl.progress(scrollPercent).pause();
};

window.addEventListener('scroll', updateParallax);

tl.play();

const cards = document.querySelectorAll('.card');
let selectedCard = null;

function selectCard(event, card) {
  // Remove the "selected" class from all cards
  cards.forEach(c => c.classList.remove('selected'));

  // Add the "selected" class to the clicked card
  card.classList.add('selected');
  selectedCard = card;

  // Move all cards to the left
  cards.forEach(c => {
    c.style.transform = 'translateX(-100%)';
  });

  // Bring the selected card to the front
  const main = document.querySelector('.main');
  main.appendChild(selectedCard);
}

// Add initial positioning for the cards
cards.forEach(c => {
  c.style.transition = 'transform 0.3s ease-out';
  c.style.transform = 'translateX(0)';
});
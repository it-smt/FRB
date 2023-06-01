'use strict'

const iconMenu = document.querySelector('.menu__icon');
const body = document.querySelector('body');
const menuLinks = document.querySelectorAll('.menu__link[data-goto]');
const menuBody = document.querySelector('.menu__body');
const navigation = document.querySelector('.nav');
if (iconMenu) {
    iconMenu.addEventListener('click', function (e) {
        iconMenu.classList.toggle('_active');
        menuBody.classList.toggle('_active');
        navigation.classList.toggle('_active');
        body.classList.toggle('_lock');
    });
}


// Прокрутка при клике

if (menuLinks.length > 0) {
    menuLinks.forEach(menuLink => {
        menuLink.addEventListener('click', onMenuLinkClick);
    });

    function onMenuLinkClick(e) {
        const menuLink = e.target;
        if (menuLink.dataset.goto && document.querySelector(menuLink.dataset.goto)) {
            const gotoBlock = document.querySelector(menuLink.dataset.goto);
            const gotoBlockValue = gotoBlock.getBoundingClientRect().top + pageYOffset - document.querySelector('header').offsetHeight;

            iconMenu.classList.remove('_active');
            menuBody.classList.remove('_active');
            navigation.classList.remove('_active');
            body.classList.remove('_lock');

            window.scrollTo({
                top: gotoBlockValue,
                behavior: "smooth"
            });
            e.preventDefault();
        }
    }
}
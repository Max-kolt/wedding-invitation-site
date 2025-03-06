var button = document.querySelector('.dress_toggle');

var girlsPhoto = document.querySelectorAll(".womphoto");
var boysPhoto = document.querySelectorAll('.manphoto');

button.addEventListener('click',
    function tooglePhotos(e) {
        console.log('togg');
        girlsPhoto.forEach(toggleElementClosed);
        boysPhoto.forEach(toggleElementClosed)
        button.textContent = button.textContent == 'мужчины' ? 'женщины' : 'мужчины';
    }
)

function toggleElementClosed (element) {
    element.classList.toggle('closed')
}
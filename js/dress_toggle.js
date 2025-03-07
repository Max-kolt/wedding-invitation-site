var button_dress = document.querySelector(".dress_toggle");

var girlsPhoto = document.querySelectorAll(".womphoto");
var boysPhoto = document.querySelectorAll(".manphoto");

button_dress.addEventListener("click", function tooglePhotos(e) {
  girlsPhoto.forEach(toggleElementClosed);
  boysPhoto.forEach(toggleElementClosed);
  button_dress.textContent =
    button_dress.textContent == "мужчины" ? "женщины" : "мужчины";
});

function toggleElementClosed(element) {
  element.classList.toggle("closed");
}

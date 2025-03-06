var menu = document.querySelector("#menu");
var close_button = document.querySelector(".close_icon");
var open_button = document.querySelector(".menu_lines");
var menu_points = document.querySelectorAll(".navigation_point");

open_button.addEventListener('click', 
function (event){
    menu.classList.remove("closed"); 
    document.scrol
}) ;

close_button.addEventListener('click', 
function(event){
    menu.classList.add("closed");
});

menu_points.forEach((element)=>{
    element.addEventListener('click', 
    function(event){
        menu.classList.add("closed");
    })
})
var request_button = document.querySelector(".send_request");
var arrow = document.querySelector(".req_arrow");

request_button.addEventListener("click", function (event) {
  let name_field = document.getElementById("name");
  let food_field = document.getElementById("eats");
  event.preventDefault();
  if (food_field.value.length < 2 || name_field.value.length < 2) {
    start_notification("Не все поля заполнены", 5000);
    return;
  }

  var data = JSON.stringify({
    name: name_field.value,
    present: document.getElementById("yes_present").checked,
    marry: document.getElementById("yes_marry").checked,
    twoday: document.getElementById("yes_want").checked,
    food: food_field.value,
  });

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "http://45.87.247.117:8080/save_form", false);
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.send(data);

  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      start_notification("Форма успешно отправлена", 5000);
      name_field.value = "";
      food_field.value = "";
      request_button.classList.add("sended");

      arrow.classList.remove("show");

      setTimeout(() => {
        request_button.classList.remove("sended");
        arrow.classList.add("show");
      }, 5000);

      console.log("Ответ сервера", xhr.responseText);
    } else {
      start_notification(
        "Ошибка сервера. Повторите попытку через 10 минут",
        5000
      );
      console.log("Error", xhr.statusText);
    }
  }

  console.log("sended data: ", data);
});

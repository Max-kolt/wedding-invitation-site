var is_visible = false;
var notification_popup = document.getElementById("notification");
var notification_text = document.querySelector(".notification__content > p");

function start_notification(text, time) {
  notification_text.innerHTML = text;

  notification_popup.classList.remove("closed");
  setTimeout(() => {
    notification_popup.classList.add("closed");
  }, time);
}

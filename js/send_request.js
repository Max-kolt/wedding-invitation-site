var button = document.querySelector('.send_request');


button.addEventListener('click', 
    function (event){
        event.preventDefault();
        var data = JSON.stringify({
            name: document.getElementById("name").value,
            present: document.getElementById('yes_present').checked,
            marry: document.getElementById('yes_marry').checked,
            twoday: document.getElementById('yes_want').checked,
            food: document.getElementById("eats").value,
        });
        
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/server, true");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(data);

        console.log(data);
    }
)


document.getElementById("weatherForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const data = {
        day: document.getElementById("day").value,
        month: document.getElementById("month").value,
        hour: document.getElementById("hour").value,
        humidity: document.getElementById("humidity").value,
        wind_speed: document.getElementById("wind_speed").value,
        cloud_cover: document.getElementById("cloud_cover").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").textContent = "Prediksi Cuaca: " + result.prediction;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

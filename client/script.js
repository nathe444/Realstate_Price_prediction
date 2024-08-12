let select = document.getElementById("select");

function getLocationNames(){
  fetch("http://localhost:5000/get_locations")
  .then(response => response.json())
  .then(data => {
    select.innerHTML = '';
    for (let i = 0; i < data['locations'].length; i++) {
      let option = document.createElement('option');
      option.value = data['locations'][i]; 
      option.textContent = data['locations'][i];
      select.appendChild(option); 
    }
  })
  .catch(error => {
    console.error('Error fetching locations:', error);
  });
}


function predictPrice() {
  let total_sqft = document.getElementById("total_sqft").value;
  let bhk = document.getElementById("bhk").value;
  let bath = document.getElementById("bath").value;
  let location = document.getElementById("select").value;
  let result = document.getElementById("result");

  let formData = new FormData();
  formData.append("total_sqft", parseFloat(total_sqft));
  formData.append("bhk", bhk);
  formData.append("bath", bath);
  formData.append("location", location);

  fetch("http://127.0.0.1:5000/predict_home_price", {
    method: 'POST',
    body: formData 
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    result.innerHTML = data.estimated_price + " Lakhs";
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

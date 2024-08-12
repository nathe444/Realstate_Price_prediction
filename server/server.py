from flask import Flask,request,jsonify
import util
app = Flask(__name__)


print(util.get_location_names())

@app.route('/get_locations')
def get_location_names():
 response = jsonify({
    'locations': util.get_location_names()
  })
 response.headers.add('Access-Control-Allow-Origin', '*')
 return response


@app.route('/predict_home_price',methods=['POST'])
def predict_price():
  sqft = float(request.form['total_sqft'])
  location = float(request.form['location'])
  bhk = float(request.form['bhk'])
  bath = float(request.form['bath'])

  response = jsonify({
    'price': util.predict_price(sqft,location,bhk,bath)
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

  
if __name__ == "__main__":
  print("server is starting..")
  util.loadArtifacts()
  app.run()
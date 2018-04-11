import requests
from flask import Flask, jsonify, render_template
from flask_cors import CORS
app = Flask(__name__, static_folder='static')

BASE_YELP = 'https://api.yelp.com/v3'
TOKEN = '7OdUTCkfo-Hoyu57HZRJnG0XEkCdxmZ8ktiIvLdbezcSd0PqzKBbUyGSwWlh8WxAjeZuWIHFMbx2wIESzqz_Dkb2INGBLW7mQe8kpDiE3AcK9akFRLY-RDKgZtzyWHYx'
CORS(app)

@app.route('/location')
def location():
   return jsonify(
      {
         'title': 'Beira Mar Shopping',
         'latitude': -27.584725,
         'longitude': -48.544890
      },
      {
         'title': 'Iguatemi Shopping',
         'latitude': -27.5901819,
         'longitude': -48.5147876
      },
      {
         'title': 'Mercado Publico',
         'latitude': -27.5971527,
         'longitude': -48.5526082
      },
      {
         'title': 'Ponte Hercilio Luz',
         'latitude': -27.593900,
         'longitude': -48.565993
      },
      {
         'title': 'Delicias Portuguesas',
         'latitude': -27.5922454,
         'longitude': -48.5470533
      }
   )


@app.route('/search/<place>')
def search(place):
   params = {'term': place, 'location': 'Florianopolis'}
   response = requests.get(
      BASE_YELP + '/businesses/search', params=params,
      headers={'Authorization': 'Bearer {}'.format(TOKEN)}
   )
   return jsonify(response.json())

@app.route('/')
def index():
   return render_template('index.html')


if __name__ == '__main__':
   app.run()

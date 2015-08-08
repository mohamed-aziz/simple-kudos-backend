

from flask import Flask
from flask import Response

import pickle
app = Flask(__name__)

@app.route('/kudos')
def kudos():
  a = pickle.load(open('kudos.p', 'rb'))
  if type(a) is int:
    a += 1
    pickle.dump(a, open('kudos.p', 'wb'))
  return ''

@app.route('/get')
def get():
  a = pickle.load(open('kudos.p', 'rb'))
  if type(a) is int:
    return str(a)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
  app.run(debug=True)

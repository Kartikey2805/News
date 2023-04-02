from flask import Flask, render_template
import requests

API_KEY = 'pub_199278bc304378ac707d94931eb5ae055ddfa'

url = 'https://newsdata.io/api/1/news?apikey=pub_199278bc304378ac707d94931eb5ae055ddfa&language=en'

response = requests.get(url)

content = response.json()
# print(content)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("tutorial.html",data=content['results'])


if __name__ == '__main__':
    app.run(debug=True)

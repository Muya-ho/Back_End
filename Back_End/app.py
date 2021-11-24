from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


app = Flask(__name__, template_folder='templates')

GoogleMaps(app, key="구글키")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count')
def count():
    return '구별 쓰레기통 개수 보기'

@app.route('/near', methods = ['GET'])
def near():
    #locations = 
    mymap = Map(
        identifier='view-side',
        #varname='mymap', 
        #style='height:720px;width:1100px;margin:0;', #hardcoded
        lat=37, # hardcoded
        lng=126, # hardcoded
        zoom=15,
        markers=[
        {
            'lat': 37.4941791,
            'lng': 126.8564982,
            'infobox': "<b>Hello World</b>"
        },
        {
            'lat': 37.4952586,
            'lng': 126.855954,
            'infobox': "<b>Hello World from other place</b>"
        }
        ]
    )
    return render_template('location.html', mymap = mymap)

@app.route('/developer')
def developer():
    return render_template('info.html')

@app.route('/test.js')
def test():
    return render_template('test.js')

if __name__ == '__main__':
    app.run(debug=True)
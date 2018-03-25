import requests
import pandas as pd
import io
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
from flask import Flask, render_template, request, redirect
from bokeh.embed import components 

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    #if request.method == 'POST':
        #ticker = request.form['ticker']
        #features = request.form['features']
        #return redirect("https://www.google.com")
        #return redirect(url_for('about'))
    return render_template('index.html')
    

@app.route('/about', methods=['GET', 'POST'])
def about():
    #ticker = 'GOOG'
    ticker = request.form['ticker']
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB.csv?column_index=4&start_date=2017-01-01&end_date=2017-12-31&order=asc&ticker='+ticker+'&api_key=Bi6LQVQYYUMzFxnjxMV8'
    urlData = requests.get(url).content
    rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    rawData.Date = pd.to_datetime(rawData.Date)
    # create a new plot with a title and axis labels
    p = figure(tools="pan,wheel_zoom,box_zoom,reset", title="Quandl WIKI EOD Stock Price - 2017", x_axis_label='Time', y_axis_label='Price', x_axis_type="datetime")

    # add a line renderer with legend and line thickness
    p.line(y = rawData.Close, x = rawData.Date, legend = (string + ' - Closing Value'), line_width=2)

    script, div = components(p)
    
    # show the results
    #show(p)
    return render_template('about.html',script=script, div=div)

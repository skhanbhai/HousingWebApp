from flask import Blueprint, render_template
import pandas as pd
import numpy as np
import os

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')

@page.route('/table')
def table():   
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files)) 
    readIn = pd.DataFrame({
        'Address':['a','b','c','d']*25,
        'Price':np.arange(1,101)*1000,
        'Closest Grocery Store':['a','b','c','d']*25,
        'Closest School':['a','b','c','d']*25,
        'e':np.arange(0,100),
        'f':np.arange(0,100),
        'g':np.arange(0,100),
        'h':np.arange(0,100),
    })
    results = list(readIn.T.to_dict().values())

    fieldnames = [key for key in results[0].keys()]
    return render_template('page/table.html', results = results, fieldnames = fieldnames, len = len)

@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')

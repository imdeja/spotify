from flask import Flask, jsonify, request
import sqlite3
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from typing import List, Tuple
from app.nearest_neighbors_recommender import predictor, feature_average
from app.models import db, parse_records, Data

def create_app():

    app = Flask(__name__)

    # accepts the cursor and the row as a tuple and returns a dictionary result and you can object column by name

    def dict_factory(cursor, row):
        d = {}
        for (idx, col) in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    # Landing Page
    @app.route('/')
    def hello_world():
        return 'Everything Works!'

    @app.route('/recommend', methods=['POST'])
    def suggest():
        data = request.get_json(force=True)
        input_data = data['track_key']

        output= predictor(input_data)
        return jsonify(output[1])

    @app.route('/features', methods=['POST'])
    def features():
        data = request.get_json(force=True)
        input_data = data['track_key']

        return jsonify(feature_average(input_data))

    @app.route('/data')
    def data():
        db_data = Data.query.all()
        data_response = parse_records(db_data)
        return jsonify(data_response)
        
    return app

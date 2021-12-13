from re import search
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
import requests

open('search_history.txt','w').close()
load_dotenv()                                                                                   
app = Flask(__name__)
api_key = os.getenv('MY_SECRET_KEY')

print(app.config['ENV'])
print(os.getenv('MY_SECRET_KEY'))


@app.route('/')
def index():                                                                                                                                                          
    return render_template('/index.html')

@app.route('/movie', methods=['GET'])
def get_movie_details():
    user_input = request.values.get('movie_title')
    api_url_bytitle = f'http://www.omdbapi.com/?apikey={api_key}&t={user_input}'
    movie_info_json = requests.get(api_url_bytitle).json()
    print(movie_info_json)
    return render_template("/movie.html", movie_info_json = movie_info_json)

@app.route('/multiple_results', methods=['GET'])
def multiple_results():
    user_input = request.values.get('movie_title')
    api_url_search = f'https://www.omdbapi.com/?apikey={api_key}&s={user_input}'
    movie_info_json_list = requests.get(api_url_search).json()
    print(movie_info_json_list)

    file = open('history.txt', 'a')
    file.write(f'{user_input}\n')
    file.close()

    if 'Error' in movie_info_json_list:
        return render_template("/invalid.html")
    elif len(movie_info_json_list['Search']) == 1:
        return redirect(url_for(get_movie_details, title=movie_info_json_list['Search'][0]['Title']) ) 
    else:
        return render_template('/multiple_results.html', movie_info_json_list=movie_info_json_list)


@app.route('/history')
def history():
    history_data = []
    with open('history.txt', 'r') as file:
        for each_data in file:
            history_data.append(each_data.rstrip())

    return render_template('history.html', history_file=history_data)


if __name__ == '__main__':
    app.run(debug=True)

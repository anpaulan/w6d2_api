from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    recipe_search = request.args.get('search')
    if recipe_search:
        search_by_name = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={recipe_search}')
        if search_by_name.status_code == 200:
            recipe = search_by_name.json()
            if not recipe['meals']:  # Check if no meals were found
                return redirect(url_for('does_not_exist'))  # Redirect to the does_not_exist route
            return render_template('index.html', meals=recipe['meals'])
        else:
            return "Cannot fetch recipe"
    return render_template('index.html', meal={})

@app.route('/does_not_exist')
def does_not_exist():
    return render_template('does_not_exist.html')

if __name__ == '__main__':
    app.run(debug=True)

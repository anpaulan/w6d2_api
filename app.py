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
            if not recipe['meals']: 
                return redirect(url_for('does_not_exist'))  
            return render_template('index.html', meals=recipe['meals'])
        else:
            return "Cannot fetch recipe"
    return render_template('index.html')

@app.route('/does_not_exist')
def does_not_exist():
    return render_template('does_not_exist.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
@app.route('/get_meal_details/<meal_id>')
def get_meal_details(meal_id):
    meal_details = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}')
    if meal_details.status_code == 200:
        meal = meal_details.json()['meals'][0]
        return render_template('meal_details.html', meal=meal)
    else:
        return "Cannot fetch meal details"
'''
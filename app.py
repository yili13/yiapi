from flask import Flask, render_template, request

from meal_service import YisMealClient

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    meals = []
    # breakpoint()
    if request.method == 'POST':
        query = request.form.get('search')
        if query:
            client = YisMealClient()
            response = client.search_by_name(name=query)
            meals = response.get('meals', [])
    return render_template('index.html', meals=meals)

@app.route('/<meal_id>', methods=['GET'])
def meal_detail(meal_id: str):
    """get the detail of a meal by id"""
    client = YisMealClient()
    response = client.look_up_by_id(meal_id)
    meals = response.get('meals', [])
    return render_template('detail.html', meal=(meals[0] if meals else None))

@app.route('/random', methods=['GET'])
def random_meal():
    """get the detail of a meal by id"""
    client = YisMealClient()
    response = client.look_up_random()
    meals = response.get('meals', [])
    return render_template('detail.html', meal=(meals[0] if meals else None))



# make the form wider, make it scroll down on submit, spinner, search bar turned to nav bar
if __name__ == '__main__':
    app.run(debug=True)


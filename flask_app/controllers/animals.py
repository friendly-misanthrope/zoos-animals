# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
from flask_app.models import animal, zoo # Import models
from flask import render_template, redirect, request, session # Import methods from Flask

# Visible Routes - ANIMALS
@app.route('/')
def animals_root_redirect():
    return redirect('/animals')

@app.route('/animals')
def view_all_animals():
    return render_template('all_animals.html', all_animals = animal.Animal.get_all_animals_with_zoos())

@app.route('/animals/new')
def add_animal():
    return render_template('add_animal_page.html', all_zoos = zoo.Zoo.get_all_zoos())

@app.route('/animals/<int:id>/view')
def view_one_animal(id):
    return render_template('/view_one_animal.html', id=id)

@app.route('/animals/<int:id>/edit')
def edit_animal(id):
    return render_template('/edit_animal_page.html', id=id)


# Hidden Routes - ANIMALS
@app.route('/animals/process_add_animal', methods=['POST'])
def process_add_animal():
    data = {
        "species": request.form['species'],
        "name": request.form['name'],
        "weight": request.form['weight'],
        "color": request.form['color'],
        "height": request.form['height'],
        "birth_date": request.form['birth_date'],
        "zoo_id": request.form['zoo_id']
    }

    animal.Animal.add_animal(data)
    return redirect('/animals')

@app.route('/process_edit_animal', methods=['POST'])
def process_edit_animal():
    return redirect('/animals')

@app.route('/animals/<int:id>/delete')
def delete_animal(id):
    # Add function in animal model to delete animal with given ID; call that function here
    return redirect('/animals')
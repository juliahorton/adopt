from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def show_all_pets():
    """Show all pets on home page."""
    pets = Pet.query.all()

    return render_template("home.html",pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add pet form and handler."""

    form = AddPetForm()

    if form.validate_on_submit():
        
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} the {species} to our adoption list!")
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)
    
@app.route("/<int:id>")
def show_pet(id):
    """Show pet details."""

    pet = Pet.query.get_or_404(id)

    return render_template("pet_details.html", pet=pet)

@app.route("/<int:id>/edit", methods=["GET","POST"])
def edit_pet(id):
    """Edit pet form and handler."""
    
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        
        flash(f"Information updated!")

        return redirect(f"/{pet.id}")

    else:
        return render_template("pet_edit_form.html", pet=pet, form=form)





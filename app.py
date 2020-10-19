from flask import Flask, request, redirect, render_template,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db,Pet
from forms import AddPetForm,EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "YOUTELLMELASTSUMMER!"
debug = DebugToolbarExtension(app)

@app.route("/")
def homepage():
    """homepage of pet lists"""
    pets= Pet.query.all()
    return render_template("home.html",pets=pets)

@app.route("/add",methods=["GET","POST"])
def add_form():

    form = AddPetForm()
    

    """validate the form """
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        newpet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)
        flash(f"Added {name} at {species}")

        """add new pet to database pets"""
        db.session.add(newpet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("add_form.html",form=form)



@app.route("/<int:id>", methods=["GET","POST"])
def show_pet_detail(id):
    """show pet detail"""
    editform = EditPetForm()
    apet = Pet.query.get_or_404(id)

    if editform.validate_on_submit():
        photo_url = editform.photo_url.data
        notes = editform.notes.data
        available = editform.available.data

        apet.photo_url = photo_url
        apet.notes = notes
        apet.available = available

        db.session.add(apet)
        db.session.commit()

        flash(f"{apet.name} updated.")

        return redirect("/")
    
    else:
        return render_template("pet_detail.html",apet=apet,editform=editform)

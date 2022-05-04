"""Views for super user, CRUD relational tables"""

from flask import redirect, render_template, session
from app import app, db

# from ..Models.User import User
from ..Models.Community import Community
from ..Models.Elevation import Elevation
from ..Models.Product import Product
from ..Models.Drafter import Drafter
from ..Models.Engineer import Engineer
from ..Models.PlatEngineer import PlatEngineer
from ..Models.PermitJurisdiction import Jurisdiction

from ..forms.NewCommunity import NewCommunity
from ..forms.NewProduct import NewProduct
from ..forms.NewElevation import NewElevation
from ..forms.NewDrafter import NewDrafter
from ..forms.NewEngineer import NewEngineer
from ..forms.NewPlatEngineer import NewPlatEngineer
from ..forms.NewJurisdiction import NewJurisdiction


@app.route('/super/new-community', methods=["GET", "POST"])
def create_new_community():

  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  form = NewCommunity()
  communities = Community.query.all()

  if form.validate_on_submit():
    # POST request
    new_community = Community(community_name=form.community_name.data)
    db.session.add(new_community)
    db.session.commit()
    return redirect('/super/new-community')

  # GET request
  return render_template('./super_temp/new_community.html', communities=communities, form=form)

@app.route('/super/products', methods=["GET", "POST"])
def create_new_product():
  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  form = NewProduct()
  products = Product.query.all()

  if form.validate_on_submit():
    # POST request
    new_product = Product(product_name=form.product_name.data)
    db.session.add(new_product)
    db.session.commit()
    return redirect('/super/products')

  # GET request
  return render_template('./super_temp/new_product.html', products=products, form=form)


@app.route('/super/elevations', methods=["GET", "POST"])
def create_new_elevation():
  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  form = NewElevation()
  elevations = Elevation.query.all()

  if form.validate_on_submit():
    # POST request
    new_elevation = Elevation(elevation_name=form.elevation_name.data)
    db.session.add(new_elevation)
    db.session.commit()
    return redirect('/super/elevations')

  # GET request
  return render_template('./super_temp/new_elevation.html', elevations=elevations, form=form)


@app.route('/super/drafters', methods=["GET", "POST"])
def create_new_drafter():

  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  form = NewDrafter()
  drafters = Drafter.query.all()

  if form.validate_on_submit():
    # POST request
    new_drafter = Drafter(drafter_name=form.drafter_name.data)
    db.session.add(new_drafter)
    db.session.commit()
    return redirect('/super/drafters')

  # GET request
  return render_template('./super_temp/new_drafter.html', drafters=drafters, form=form)


@app.route('/super/engineers', methods=["GET", "POST"])
def create_new_engineer():

  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  form = NewEngineer()
  engineers = Engineer.query.all()

  if form.validate_on_submit():
    # POST request
    new_engineer = Engineer(engineer_name=form.engineer_name.data)
    db.session.add(new_engineer)
    db.session.commit()
    return redirect('/super/engineers')

  # GET request
  return render_template('./super_temp/new_engineer.html', engineers=engineers, form=form)


@app.route('/super/platengineers', methods=["GET", "POST"])
def create_new_platengineer():

  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  form = NewPlatEngineer()
  platengineers = PlatEngineer.query.all()

  if form.validate_on_submit():
    # POST request
    new_platengineer = PlatEngineer(platengineer_name=form.plat_engineer_name.data)
    db.session.add(new_platengineer)
    db.session.commit()
    return redirect('/super/platengineers')

  # GET request
  return render_template('./super_temp/new_platengineer.html', platengineers=platengineers, form=form)


@app.route('/super/jurisdictions', methods=["GET", "POST"])
def create_new_jurisdictions():

  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  form = NewJurisdiction()
  jurisdictions = Jurisdiction.query.all()

  if form.validate_on_submit():
    # POST request
    new_jurisdiction = Jurisdiction(jurisdiction_name=form.jurisdiction_name.data)
    db.session.add(new_jurisdiction)
    db.session.commit()
    return redirect('/super/jurisdictions')

  # GET request
  return render_template('./super_temp/new_jurisdiction.html', jurisdictions=jurisdictions, form=form)


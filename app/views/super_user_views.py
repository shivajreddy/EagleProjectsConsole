"""Views for super user, CRUD relational tables"""

from flask import redirect, render_template, session
from app import app, db

# from ..Models.User import User
from ..Models.Community import Community
from ..Models.Drafter import Drafter
from ..Models.Engineer import Engineer
from ..Models.PlatEngineer import PlatEngineer
from ..Models.PermitJurisdiction import Jurisdiction

from ..forms.NewCommunity import NewCommunity
from ..forms.NewDrafter import NewDrafter
from ..forms.NewEngineer import NewEngineer
from ..forms.NewPlatEngineer import NewPlatEngineer
from ..forms.NewJurisdiction import NewJurisdiction


@app.route('/super/new-community', methods=["GET", "POST"])
def create_new_community():
  """community table"""

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


@app.route('/super/drafters', methods=["GET", "POST"])
def create_new_drafter():
  """Drafters table"""

  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')
  
  # form = NewCommunity()
  # communities = Community.query.all()
  form = NewDrafter()
  drafters = Drafter.query.all()

  if form.validate_on_submit():
    # POST request
    # new_community = Community(community_name=form.community_name.data)
    new_drafter = Drafter(drafter_name=form.drafter_name.data)
    db.session.add(new_drafter)
    db.session.commit()
    return redirect('/super/drafters')

  # GET request
  # return render_template('./super_temp/new_community.html', communities=communities, form=form)
  return render_template('./super_temp/new_drafter.html', drafters=drafters, form=form)
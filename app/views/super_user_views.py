"""Views for super user, CRUD relational tables"""

from flask import redirect, render_template, session
from app import app, db

# from ..Models.User import User
from ..Models.Community import Community
from ..forms.NewCommunity import NewCommunity


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


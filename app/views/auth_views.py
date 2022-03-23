"""views for authentication"""
from app import app, db
from flask import flash, session, redirect, render_template

from ..Models.User import User
from ..forms.LoginForm import RegistrationForm, LoginForm

#? User Registration
@app.route('/register', methods=["GET", "POST"])
def sign_in():
  form = RegistrationForm()

  # validate form
  if form.validate_on_submit():
    
    if User.query.filter_by(email=form.email.data).first():
      flash(" already exists", f"{form.email.data}")
      return redirect('/sign-in')

    new_user = User.register(form.email.data, form.password.data)
    flash(f"Your account has been created, with {new_user.email}", "User already exists")
    session['user_email'] = new_user.email
    session['editor'] = new_user.editor
    session['super_editor'] = new_user.super_editor
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

  return render_template('sign_up.html', form_data=form)



#? User Log-In
@app.route('/sign-in', methods=["GET", "POST"])
def register():
  form = LoginForm()

  if form.validate_on_submit():
    usr = User.query.filter_by(email=form.email.data).first()
    if not usr:
      flash("not found!", f"{form.email.data}")
      return redirect('/sign-in')
    if usr.authenticate(form.email.data, form.password.data):

      session['user_email'] = usr.email
      session['editor'] = usr.editor
      session['super_editor'] = usr.super_editor

      return redirect('/')
    flash(": Password incorrect", f"{form.email.data}")
    return redirect('/sign-in')
    
  return render_template('login.html', form_data=form)


#? Log out
@app.route('/logout', methods=["POST"])
def logout():
  flash("successfully logged out.", session['user_email'])
  if 'user_email' in session:
    session.pop('user_email')
  if 'editor' in session:
    session.pop('editor')
  return redirect('/sign-in')


@app.errorhandler(404)
def not_found_404(e):
  return render_template('404.html')
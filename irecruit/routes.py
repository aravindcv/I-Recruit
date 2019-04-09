from flask import render_template, url_for, flash, redirect, request, jsonify
from flask_bcrypt import Bcrypt
from irecruit import app, db, bcrypt
from irecruit.forms import AdminloginForm, AdminForm, LoginForm, DetailsForm
from irecruit.models import Admin, User, Skill
from flask_login import login_user, current_user, logout_user, login_required, user_logged_in

flag = 0

@app.route("/adminlogin", methods = ['POST', 'GET'])
def adminlogin():
    form = AdminloginForm()
    if form.validate_on_submit():
        if form.username.data == "aravindcv" and form.password.data == "password":
            global flag
            flag = 1
            db.create_all()
            flash('Admin verified!', 'success')
            return redirect(url_for('admin'))
    return render_template('adminlogin.html', title='Admin-Login', form=form)

@app.route("/admin", methods = ['POST', 'GET'])
def admin():
    if flag:
        form = AdminForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = Admin(email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('User added to the database successfully', 'success')
    else:
        flash('Admin not logged in!', 'danger')
        return redirect(url_for('adminlogin'))
    return render_template('admin.html', title='Admin', form=form)



@app.route("/", methods = ['POST', 'GET'])
@app.route("/home", methods = ['POST', 'GET'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You can enter your details now!', 'success')
            return redirect(url_for('details'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('home'))
    return render_template('login1.html', title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/details", methods = ['POST', 'GET'])
def details():
    if current_user.is_authenticated:
        form = DetailsForm()
        if form.validate_on_submit():
            try:
                user = User(firstname=form.firstname.data, lastname=form.lastname.data, dob=form.dob.data, user_id = current_user.id)
                skills = Skill(skill1=form.skill1.data, level1=form.level1.data,
                                skill2=form.skill2.data, level2=form.level2.data,
                                skill3=form.skill3.data, level3=form.level3.data,
                                skill4=form.skill4.data, level4=form.level4.data, user_id = current_user.id)
                db.session.add(user)
                db.session.add(skills)
                db.session.commit()
                flash('Your details has been submitted! You are now able to take the test', 'success')
                return redirect(url_for('test'))
            except:
                db.session.rollback()
                flash('Your details already exist! You can\'t retake test', 'danger')
                return redirect(url_for('logout'))
    else:
        flash('You are not logged in! Please login', 'danger')
        return redirect(url_for('home'))
    return render_template('details.html', title='Details', form=form)

@app.route("/test", methods = ['POST', 'GET'])
def test():
    print('')
    if current_user.is_authenticated:
        user = User.query.get(current_user.id)
    else:
        flash('You are not logged in! Please login', 'danger')
        return redirect(url_for('home'))
    return render_template('test.html', title='Test', user=user)

@app.route('/view_users')
def view_users():
    db.create_all()
    users = Admin.query.all()
    return render_template('view_users.html', users = users)


flag = 0

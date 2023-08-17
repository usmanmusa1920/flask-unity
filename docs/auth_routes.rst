:tocdepth: 2

Custome auth
############

Custom authentication for users

In this chapter we are going to see how we can write a custom authentication for users which will replace the default route for our `auth` pages and instead of rendering the `wtforms` views, we are to use html form. To do so, flask_unity already have html form for that available in the **[admin_register.html, admin_login.html, admin_change_password.html]**, now what remain for us is to create an app (`custom_auth`) just like the way we create the exam app::

    python thunder.py create_app -a custom_auth

after that, paste the following in the `custom_auth` views.py file:

First we are to replace the top import with the following::

    import re
    import os
    import secrets
    from werkzeug.utils import secure_filename
    from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, send_file
    from flask_unity.utils import footer_style, template_dir, static_dir
    from flask_login import login_user, current_user, logout_user, fresh_login_required, login_required
    from flask_unity.contrib import db, bcrypt
    from flask_unity.auth.models import User
    # from .models import <app_models>
    # from .forms import <model_form>


    UPLOAD_FOLDER = os.environ.get('FLASK_UPLOAD_FOLDER')
    ORIGIN_PATH = os.environ.get('FLASK_ORIGIN_PATH')
    ALLOWED_EXTENSIONS = os.environ.get('FLASK_ALLOWED_EXTENSIONS')

**Route for register:** the default route of `adminRegister` can be replace with::

    @custom_auth.route('/admin/register/', methods=['POST', 'GET'])
    @login_required
    def adminRegister():
        """
        The `admin_register.html` below is located in the flask_unity package (templates/default_page/admin_register.html)
        """
        if request.method == 'POST':
            username  = request.form['username']
            email  = request.form['email']
            password1 = request.form['password1']
            password2 = request.form['password2']
            # username check
            check_username = User.query.filter_by(username=username).first()
            if check_username:
                flash(f'This username `{check_username}` has been taken!', 'error')
                return redirect(url_for('custom_auth.adminRegister'))
            # email check
            check_email = User.query.filter_by(email=email).first()
            if check_email:
                flash(f'This email `{check_email}` is taken, choose a different one.', 'error')
                return redirect(url_for('custom_auth.adminRegister'))
            # checking email pattern using regex
            pattern = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
            if not re.match(pattern, email):
                flash(f'Please use a valid email', 'error')
                return redirect(url_for('custom_auth.adminRegister'))
            # password check
            if len(password1) < 6 or len(password2) < 6:
                flash('Password must be not less than 6 character', 'error')
                return redirect(url_for('custom_auth.adminRegister'))
            if password1 == password2:
                hashed_password = bcrypt.generate_password_hash(password2).decode('utf-8')
                user_obj = User(username=username, email=email, password=hashed_password)
                db.session.add(user_obj)
                db.session.commit()
                flash(f'Account for {username} has been created!', 'info')
                return redirect(url_for('custom_auth.adminLogin'))
            else:
                flash(f'The two password fields didn\'t match', 'error')
        context = {
            'head_title': 'admin register',
            'footer_style': footer_style,
        }
        return render_template('admin_register.html', context=context)


**Route for login** the default route of `adminLogin` can be replace with::

    @custom_auth.route('/admin/login/', methods=['POST', 'GET'])
    def adminLogin():
        """
        The `admin_login.html` below is located in the flask_unity package (templates/default_page/admin_login.html)
        """
        if current_user.is_authenticated:
            return redirect(url_for('base.index'))
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                """
                    Parameters:
                    user (object) - The user object to log in.

                    remember (bool) - Whether to remember the user after their session expires. Defaults to False.

                    duration (datetime.timedelta) - The amount of time before the remember cookie expires. If None the value set in the settings is used. Defaults to None.

                    force (bool) - If the user is inactive, setting this to True will log them in regardless. Defaults to False.

                    fresh (bool) - setting this to False will log in the user with a session marked as not “fresh”. Defaults to True.
                """
                login_user(user, remember=True)
                flash('You are now logged in!', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('admin.index'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'error')
        context = {
            'head_title': 'admin login',
            'footer_style': footer_style,
        }
        return render_template('admin_login.html', context=context)


**Route for change password** the default route of `adminChangePassword` can be replace with::

    @custom_auth.route('/admin/change/password/', methods=['POST', 'GET'])
    @fresh_login_required
    def adminChangePassword():
        """
        The `admin_change_password.html` below is located in the flask_unity package (templates/default_page/admin_change_password.html)
        """
        if request.method == 'POST':
            old_password = request.form['old_password']
            password1 = request.form['password1']
            password2 = request.form['password2']
            # password check
            if len(password1) < 6 or len(password2) < 6:
                flash('Password must be not less than 6 character', 'error')
                return redirect(url_for('custom_auth.adminChangePassword'))
            user = User.query.filter_by(username=current_user.username).first()
            if user and bcrypt.check_password_hash(user.password, old_password):
                if password1 == password2:
                    hashed_password = bcrypt.generate_password_hash(password2).decode('utf-8')
                    user.password = hashed_password
                    db.session.commit()
                    flash('Your password has changed!', 'success')
                    return redirect(url_for('custom_auth.adminLogin'))
                else:
                    flash('The two password fields didn\'t match', 'error')
            else:
                flash('Cross check your login credentials!', 'error')
        context = {
            'head_title': 'admin change password',
            'footer_style': footer_style,
        }
        return render_template('admin_change_password.html', context=context)


**Route for logout** the default route of `adminLogout` can be replace with::

    @custom_auth.route('/custom_admin/logout/', methods=['POST', 'GET'])
    @login_required
    def adminLogout():
        logout_user()
        flash('You logged out!', 'info')
        return redirect(url_for('custom_auth.adminLogin'))
    

**Route and functions for changing image and it route** can be replace with::

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

    @custom_auth.route('/profile_image/<path:filename>')
    @login_required
    def profile_image(filename):
        """
        This function help to show current user profile image, it won't download it
        like the `download_file` function below does
        """
        return send_file(UPLOAD_FOLDER + '/' + filename)
    

    @custom_auth.route('/media/<path:filename>')
    @login_required
    def download_file(filename):
        """
        If we use this to show current user profile image, it won't show instead it will download it,
        so it meant for downloading media file
        """
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
    

    def picture_name(pic_name):
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(pic_name)
        picture_fn = random_hex + f_ext
        new_name = _ + '_' + picture_fn
        return new_name
    

    @custom_auth.route('/custom_admin/change_profile_image/', methods=['POST', 'GET'])
    @login_required
    def changeProfileImage():
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_name = picture_name(filename)
                file.save(os.path.join(UPLOAD_FOLDER, file_name))
                user = User.query.filter_by(username=current_user.username).first()
                if user:
                    if user.user_img != 'default_img.png':
                        r = str(ORIGIN_PATH) + '/media/' + user.user_img
                        if os.path.exists(r):
                            os.remove(r)
                    user.user_img = file_name
                    db.session.commit()
                flash('Your profile image has been changed!', 'success')
                return redirect(url_for('base.index')) # it will redirect to the home page
        context = {
            'head_title': 'admin change profile image',
            'footer_style': footer_style,
        }
        return render_template('admin_change_profile_image.html', context=context)
    
    
After all of the above, now open your project routes.py file (schoolsite/routes.py) and import your `custom_auth` blueprint::

    from custom_auth.views import custom_auth

then pass it into the reg_blueprints list in other to register it by::

    reg_blueprints = [
        blueprint.default,
        blueprint.errors,
        blueprint.auth,
        base,
        exam,
        custom_auth,
    ]

This will overwrite the default auth system for those routes. You can open the default admin page within your project (templates/admin/index.html) and overite it with::

  <!-- @flask_unity, schoolsite (project) admin index.html page -->
  {% extends 'admin/master.html' %}
  {% block body %}
    <a href="/">Go to schoolsite home page</a>
    <br>
    {% if current_user.is_authenticated %}
      <a href="{{ url_for('custom_auth.adminLogout') }}">logout</a>
      <br>
      <a href="{{ url_for('custom_auth.adminChangePassword') }}">change password</a>
      <br>
      <a href="{{ url_for('custom_auth.adminRegister') }}">register</a>
      <br>
      <a href="{{ url_for('custom_auth.changeProfileImage') }}">change image</a>
    {% else %}
      <a href="{{ url_for('custom_auth.adminLogin') }}">login</a>
    {% endif %}
  {% endblock body %}


Even the **User** model can be overwrite, but make sure to go all the files and import it from the custom_auth model instead of from flask_unity. Note: ``the creation of a user using the python thunder.py create_user command won't work`` for the custom model.

**Source code** for the `custom auth` is available at official `github <https://github.com/usmanmusa1920/flask-unity/tree/master/example/custom_auth>`_ repository of the project.

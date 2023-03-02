:tocdepth: 2

Auth routes
###########

In this chapter we are going to see how we can replace the default route for our `auth` pages instead of rendering the `wtforms` (in the auth package of our project `auth/routes.py`) to use html form. To do so, sakyum already have html form for that available in the **[admin_register.html, admin_login.html, admin_change_password.html]**, now what remain for us is just to replace the default routes in the `auth/routes.py` with the following:

**Route for register:** the default route of `adminRegister` can be replace with::

  @auth.route("/admin/register/", methods=["POST", "GET"])
  def adminRegister():
    """
      the `admin_register.html` below is located in the sakyum package (templates/default_page/admin_register.html)
    """
    if request.method == "POST":
      username  = request.form["username"]
      email  = request.form["email"]
      password1 = request.form["password1"]
      password2 = request.form["password2"]
      # username check
      check_username = User.query.filter_by(username=username).first()
      if check_username:
        flash(f"This username `{check_username}` has been taken!", "error")
        return redirect(url_for("auth.adminRegister"))
      # email check
      check_email = User.query.filter_by(email=email).first()
      if check_email:
        flash(f"This email `{check_email}` is taken, choose a different one.", "error")
        return redirect(url_for("auth.adminRegister"))
      # checking email pattern using regex
      pattern = re.compile(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")
      if re.match(pattern, email):
        pass
      if not re.match(pattern, email):
        flash(f"Please use a valid email", "error")
        return redirect(url_for("auth.adminRegister"))
      # password check
      if len(password1) < 6 or len(password2) < 6:
        flash("Password must be not less than 6 character", "error")
        return redirect(url_for("auth.adminRegister"))
      if password1 == password2:
        hashed_password = bcrypt.generate_password_hash(password2).decode("utf-8")
        user_obj = User(username=username, email=email, password=hashed_password)
        db.session.add(user_obj)
        db.session.commit()
        flash(f"Account for {username} has been created!", "info")
        return redirect(url_for("auth.adminLogin"))
      else:
        flash(f"The two password fields didn't match", "error")
        return redirect(url_for("auth.adminLogin"))
    context = {
      "head_title": "admin register",
      "footer_style": footer_style,
    }
    return render_template("admin_register.html", context=context)


**Route for login** the default route of `adminLogin` can be replace with::

  @auth.route("/admin/login/", methods=["POST", "GET"])
  def adminLogin():
    """
      the `admin_login.html` below is located in the sakyum package (templates/default_page/admin_login.html)
    """
    if current_user.is_authenticated:
      flash("You are already logged in!", "success")
      return redirect(url_for("base.index"))
    if request.method == "POST":
      username = request.form["username"]
      password = request.form["password"]
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
        flash("You are now logged in!", "success")
        next_page = request.args.get("next")
        return redirect(next_page) if next_page else redirect(url_for("admin.index"))
      else:
        flash("Login Unsuccessful. Please check username and password", "error")
    context = {
      "head_title": "admin login",
      "footer_style": footer_style,
    }
    return render_template("admin_login.html", context=context)


**Route for change password** the default route of `adminChangePassword` can be replace with::

  @auth.route("/admin/change/password/", methods=["POST", "GET"])
  @fresh_login_required
  def adminChangePassword():
    """
      the `admin_change_password.html` below is located in the sakyum package (templates/default_page/admin_change_password.html)
    """
    if request.method == "POST":
      old_password = request.form["old_password"]
      password1 = request.form["password1"]
      password2 = request.form["password2"]
      # password check
      if len(password1) < 6 or len(password2) < 6:
        flash("Password must be not less than 6 character", "error")
        return redirect(url_for("auth.adminChangePassword"))
      elif password2 != password1:
        flash("The two password fields didn't match", "error")
        return redirect(url_for("auth.adminChangePassword"))
      user = User.query.filter_by(username=current_user.username).first()
      if user and bcrypt.check_password_hash(user.password, old_password):
        if password1 == password2:
          hashed_password = bcrypt.generate_password_hash(password2).decode("utf-8")
          user.password = hashed_password
          db.session.commit()
        flash("Your password has changed!", "success")
        return redirect(url_for("auth.adminLogin"))
      else:
        flash("Cross check your login credentials!", "error")
    context = {
      "head_title": "admin change password",
      "footer_style": footer_style,
    }
    return render_template("admin_change_password.html", context=context)


Lastly the default route for **logout** we are not to change it, since it has nothing to render in a page.

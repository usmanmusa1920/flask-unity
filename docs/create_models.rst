:tocdepth: 2

App models
##########

This will be a continuation of the `quick start <https://flask-unity.readthedocs.io/en/latest/quick_start.html>`_. As we saw in the `quick start` we create a project called **schoolsite** and an app inside the project called **exam**. Taking from there let continue by creating models in our **exam** app.

**Note** that, you can write your views or models like the way you usually write them when using flask without flask-unity. It work great, nothing change.

Now we are going to create models for our **exam** app, the models are going to be two `ExamQuestionModel` and `ExamChoiceModel`

To create these two models we have to go into our **exam** app models.py **exam/models.py**. We will notice some default import::

    from datetime import datetime
    from schoolsite.config import db

Now below we are to start defining our model, let start with **ExamQuestionModel** model which will look like::

    class ExamQuestionModel(db.Model):
        """ Exam default Question model """
        id = db.Column(db.Integer, primary_key=True)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        # the user field is the user who create the question and he is in the `User` models of auth
        user = db.relationship('User', backref='user')
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        title = db.Column(db.String, nullable=False)
        summary = db.Column(db.Text, nullable=False)
        choices = db.relationship('ExamChoiceModel', backref='selector', lazy=True)

        def __str__(self):
            return f'{self.title}'

        def __repr__(self):
            return f'{self.title}'
        
        # the `ExamChoiceModel` is the choice model class below
        # the `selector` is the attribute that we can use to get selector who choose the choice
        # the `lazy` argument just define when sqlalchemy loads the data from the database

Now let define the **ExamChoiceModel** model which will look like::

    class ExamChoiceModel(db.Model):
        """ Exam default Choice model """
        id = db.Column(db.Integer, primary_key=True)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        question_id = db.Column(db.Integer, db.ForeignKey('exam_question_model.id'), nullable=False)
        # you can pass a keyword argument of `unique=True` in the below choice_text field
        # that will make it unique across the entire table of choice
        choice_text = db.Column(db.String(100), nullable=False)

        def __str__(self):
            return f'{self.choice_text}'

        def __repr__(self):
            return f'{self.choice_text}'

After pasting them, save the file. Goto `env.py` file inside migration directory `(migrations/env.py)` and import these two models below the import of db, like::
    
    from flask_unity.contrib import db
    from exam.models import ExamQuestionModel, ExamChoiceModel
    target_metadata = db.Model.metadata
    
From here we can now create a migration for our `ExamQuestionModel and ExamChoiceModel` models by::
    
    flaskunity db makemigrations
    flaskunity db migrate
    
Explore and check how to `create migration <https://flask-unity.readthedocs.io/en/latest/database.html>`_ in flask_unity, now let just play with `api`.

Play with api
-------------

Before we move further let us play with the model api. This is the continuation from the last tutorial where we stop, when we make debug value to be `True` after registering the app ( `last tutorial <https://flask-unity.readthedocs.io/en/latest/quick_start.html#register-an-app>`_ )

Go into the python **shell** ( python interpreter ), make sure you are within that directory you boot up the server by typing **python**, once you are in the interpreter, start by importing your **db** and **bcrypt** (for password hash) instance from project package (schoolsite), and also import the models you create for your app in `exam/models.py` and the default User model located in `auth.models.py`::

    from flask_unity.contrib import bcrypt
    from flask_unity.auth.models import User
    from schoolsite.config import db
    from exam.models import ExamQuestionModel, ExamChoiceModel

.. note::
    
    Don't call the `create_all()` method of **db** which will try to create the tables of our models and database (if it doesn't create db file). by running `db.create_all()`. This already populated with alembic (alembic take care).

After that let us create three users instance, that will be able to create question and choice of the **ExamQuestionModel** and **ExamChoiceModel** model::

    user1_hashed_pwd = bcrypt.generate_password_hash('123456').decode('utf-8')
    user1 = User(username='backend-developer', email='developer@backend.com', password=user1_hashed_pwd)

    user2_hashed_pwd = bcrypt.generate_password_hash('123456').decode('utf-8')
    user2 = User(username='frontend-developer', email='developer@frontend.com', password=user2_hashed_pwd)

    user3_hashed_pwd = bcrypt.generate_password_hash('123456').decode('utf-8')
    user3 = User(username='quantum-developer', email='developer@quantum.com', password=user3_hashed_pwd)

Now we are to add and commit those users in our database::

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

To make sure our users have been added in our database let query the entire User model of our project by::

    User.query.all()
    # [User('backend-developer', 'developer@backend.com'), User('frontend-developer', 'developer@frontend.com'), User('quantum-developer', 'developer@quantum.com')]

Yes, our users are in the database, good jod. The next thing now is to start creating our Questions and commit them to our database::

    q1 = ExamQuestionModel(title='At which year Neil Armstrong landed in the moon?', summary='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Facilis culpa fugiat pariatur nihil, sint, minus similique ea sit, id esse odio. Nam dolore cumque eum et earum laudantium quae quo.', user=user1)
    q2 = ExamQuestionModel(title='What is odd in the choice?', summary='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Facilis culpa fugiat pariatur nihil, sint, minus similique ea sit, id esse odio. Nam dolore cumque eum et earum laudantium quae quo.', user=user2)
    q3 = ExamQuestionModel(title='What is not related to quantum?', summary='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Facilis culpa fugiat pariatur nihil, sint, minus similique ea sit, id esse odio. Nam dolore cumque eum et earum laudantium quae quo.', user=user3)

    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.commit()

To make sure our `questions` are in the database let query them to see by::

    ExamQuestionModel.query.all()
    # [At which year Neil Armstrong landed in the moon?, What is odd in the choice?, What is not related to quantum?]

Yes, our questions are in the database, good jod. We are to capture our questions `id` (q1, q2 and q3) since they are the once we are going to link to each choice::

    the_q1 = ExamQuestionModel.query.get_or_404(1)
    the_q2 = ExamQuestionModel.query.get_or_404(2)
    the_q3 = ExamQuestionModel.query.get_or_404(3)

    # choices for our first question
    c1_1 = ExamChoiceModel(choice_text='In 1969', question_id=the_q1.id)
    c1_2 = ExamChoiceModel(choice_text='In 1996', question_id=the_q1.id)
    c1_3 = ExamChoiceModel(choice_text='In 2023', question_id=the_q1.id)
    c1_4 = ExamChoiceModel(choice_text='In 2007', question_id=the_q1.id)

    # choices for our second question
    c2_1 = ExamChoiceModel(choice_text='python', question_id=the_q2.id)
    c2_2 = ExamChoiceModel(choice_text='java', question_id=the_q2.id)
    c2_3 = ExamChoiceModel(choice_text='linux', question_id=the_q2.id)
    c2_4 = ExamChoiceModel(choice_text='ruby', question_id=the_q2.id)

    # choices for our third question
    c3_1 = ExamChoiceModel(choice_text='qubit', question_id=the_q3.id)
    c3_2 = ExamChoiceModel(choice_text='entanglement', question_id=the_q3.id)
    c3_3 = ExamChoiceModel(choice_text='bit', question_id=the_q3.id)
    c3_4 = ExamChoiceModel(choice_text='superposition', question_id=the_q3.id)

    # Now let add and commit the choice into database::
    db.session.add(c1_1)
    db.session.add(c1_2)
    db.session.add(c1_3)
    db.session.add(c1_4)

    db.session.add(c2_1)
    db.session.add(c2_2)
    db.session.add(c2_3)
    db.session.add(c2_4)

    db.session.add(c3_1)
    db.session.add(c3_2)
    db.session.add(c3_3)
    db.session.add(c3_4)

    db.session.commit()

We can see choices related to our question number one (1) by::

    ExamQuestionModel.query.get_or_404(1).choices
    # [In 1969, In 1996, In 2023, In 2007]

To see many other method related to our `ExamQuestionModel.query` by passing it into `dir()` function::

    dir(ExamQuestionModel.query)

To see all choices in our database::

    ExamChoiceModel.query.all()
    # [In 1969, In 1996, In 2023, In 2007, python, java, linux, ruby, qubit, entanglement, bit, superposition]

Also like the `ExamQuestionModel.query` we see above, we can see many other method related to our `ExamChoiceModel.query` by passing it into `dir()` function::

    dir(ExamChoiceModel.query)

Lastly let us make a loop over all question and print each question choices::

    for question in ExamQuestionModel.query.all():
        question
        for choice in question.choices:
            print('\t', f'{choice.id}: ', choice)

  # At which year Neil Armstrong landed in the moon?
  #     1:  In 1969
  #     2:  In 1996
  #     3:  In 2023
  #     4:  In 2007
  # What is odd in the choice?
  #     5:  python
  #     6:  java
  #     7:  linux
  #     8:  ruby
  # What is not related to quantum?
  #     9:  qubit
  #     10:  entanglement
  #     11:  bit
  #     12:  superposition

Since we insert something into the database, let move on, on how we can make those record to be display in the admin page (by registering the models), because if now we logout from the python interpreter and boot up the server **python run.py boot -d True** then navigate to admin page we won't be able to see those models. We can do so below:

Register our models to admin
----------------------------

In other to register our model, we are to open a sub project folder and open the **config.py** file we see there **(schoolsite/config.py)**, within create_app function in the file, we are to import our app models (**ExamQuestionModel**, **ExamChoiceModel**) that we want to register, above the method that will create the tables **db.create_all()** and we will see a commented prototype above it::

    """ You will need to import models themselves here! """
    from flask_unity.auth.models import User
    from flask_unity.auth.admin import UserAdminView
    from exam.models import ExamQuestionModel, ExamChoiceModel
    # from <app_name>.admin import <admin_model_view>

then we will append the models in the **reg_models = []** list within **admin_runner** function (inner function of the create_app function)::

    # rgister model to admin direct by passing every model that you
    # want to manage in admin page in the below list (reg_models)
    reg_models = [
        # User,
        ExamQuestionModel,
        ExamChoiceModel,
    ]

That will register our model in the admin page and we will be able to see it if we visit the admin page now! But this kind of registering admin model is not convenient, the convenient way is to use what is called admin model view.

Register model in the form of admin model view
----------------------------------------------

We can register our model in the form of model view by grouping models that are related.

To create these model view we have to go into our app admin.py **exam/admin.py**. We will notice some default import::

    from flask_login import current_user
    from flask import redirect, request, url_for
    from flask_admin.contrib.sqla import ModelView

Now below we are to start defining our model view, I will call the model view **QuestionChoiceAdminView** which will look like::

    class QuestionChoiceAdminView(ModelView):
        can_delete = True  # enable model deletion
        can_create = True  # enable model deletion
        can_edit = True  # enable model deletion
        page_size = 50  # the number of entries to display on the list view

        def is_accessible(self):
            return current_user.is_authenticated

        def inaccessible_callback(self, name, **kwargs):
            # redirect to login page if user doesn't have access
            return redirect(url_for('auth.adminLogin', next=request.url))

The `is_accessible` method will check if a user is logged in, in other to show the `QuestionChoiceAdminView` model in the admin page, else it just show the plain admin page without the `QuestionChoiceAdminView`.

The `inaccessible_callback` method will redirect user (who is not logged in) to the login page of the admin. Hit over `flask-admin <https://flask-admin.readthedocs.io>`_ for more clarifications.

In other to register our model view, open the `config.py` file (schoolsite/config.py) and import our admin model view (`QuestionChoiceAdminView`) below the import of our `ExamQuestionModel` and `ExamChoiceModel`  which look like::

    """ You will need to import models themselves here! """
    from flask_unity.auth.models import User
    from flask_unity.auth.admin import UserAdminView
    from exam.models import ExamQuestionModel, ExamChoiceModel
    from exam.admin import QuestionChoiceAdminView
    
Now comment the **ExamQuestionModel** and **ExamChoiceModel** in the `reg_models` list, just like the way we comment the `User` in the list, because if we didn't comment it and we register our `QuestionChoiceAdminView` that mean we register `ExamQuestionModel and ExamChoiceModel` twice and that will trow an error::

    # rgister model to admin direct by passing every model that you
    # want to manage in admin page in the below list (reg_models)
    reg_models = [
        # User,
        # ExamQuestionModel,
        # ExamChoiceModel,
    ]

go below the function we call **adminModelRegister** in (within admin_runner function) after registering  our `UserAdminView` and call the admin method called **add_view** and then pass your model view class as an argument, also pass an arguments in the model view class, the first argument is the model class, the second is the **db.session**, and then last give it a category (key word argument) in our case we will call it **category='Question-Choice' like::

    admin.add_view(QuestionChoiceAdminView(ExamQuestionModel, db.session, name='Questions', category='Question-Choice'))
    admin.add_view(QuestionChoiceAdminView(ExamChoiceModel, db.session, name='Choices', category='Question-Choice'))

Save the file, that will register your related model in the admin page and you will see them if you vist the admin page `http://127.0.0.1:5000/admin`, only if you are logged in because of `is_accessible` method.

Now let navigate to `http://127.0.0.1:5000/login` and login using one of the user credential, we created when we were in the python interpreter (shell), the one (user credential) that we are going to use is for the `backend-developer` (username: **backend-developer**, password: **123456**).

After we logged in, now if we navigate to `http://127.0.0.1:5000/admin` we are able to see our `QuestionChoiceAdminView` view in the form of drop-down menu, if we click it, it will show list containing `Questions  and Choices` only, since the are the only once associated with that mode admin view. Now click the `Questions` this will show list of questions we have inserted in the python shell.

Bonus point
-----------

For you to get out of lock when dropping a unique field in your table, make sure you dont do like:

.. code-block:: python

    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        username = db.Column(db.String(20), unique=True, nullable=False)
        user_img = db.Column(db.String(255), default='default_img.png')
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(255), nullable=False)
        authenticated = db.Column(db.Boolean, default=False)
        is_superuser = db.Column(db.Boolean, default=False)
        is_admin = db.Column(db.Boolean, default=False)
    
instead do:

.. code-block:: python

    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        username = db.Column(db.String(20), nullable=False)
        user_img = db.Column(db.String(255), default='default_img.png')
        email = db.Column(db.String(120), nullable=False)
        password = db.Column(db.String(255), nullable=False)
        authenticated = db.Column(db.Boolean, default=False)
        is_superuser = db.Column(db.Boolean, default=False)
        is_admin = db.Column(db.Boolean, default=False)
        db.UniqueConstraint('username', name='uq_user_account_username')
        db.UniqueConstraint('email', name='uq_user_account_email')

The above field that are conrcerned is `username` and `email` fields, look and compare.

**Source code** for the `app models` is available at official `github <https://github.com/usmanmusa1920/flask-unity/tree/master/example/app_models>`_ repository of the project.

See more on how to write model view class at `Flask-Admin <https://flask-admin.readthedocs.io/en/latest/introduction/#customizing-built-in-views>`_ documentation.

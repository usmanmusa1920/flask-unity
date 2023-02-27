:tocdepth: 2

App models
##########

Now we are going to create models for our exam app, the models are going to be two **ExamQuestionModel** and **ExamChoiceModel**

To create these two models we have to go into our app models.py **exam/models.py**. We will notice some default import::

    from datetime import datetime
    from Schoolsite.config import db

Now below we are to start defining our model, I will first start with **ExamQuestionModel** model which will look like::

    class ExamQuestionModel(db.Model):
      """ Exam default Question model """
      id = db.Column(db.Integer, primary_key=True)
      date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      # the user field is the user who create the question and he is in the `User` models of auth
      user = db.relationship("User", backref="user")
      user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
      question_text = db.Column(db.Text, nullable=False)
      choices = db.relationship('ExamChoiceModel', backref='selector', lazy=True)

      def __str__(self):
        return f"Question {self.id}: {self.question_text}"

      def __repr__(self):
        return f"Question {self.id}: {self.question_text}"
        
      # the `ExamChoiceModel` is the choice model class below
      # the `selector` is the attribute that we can use to get selector who choose the choice
      # the `lazy` argument just define when sqlalchemy loads the data from the database

Now I will define the **ExamChoiceModel** model which will look like::

    class ExamChoiceModel(db.Model):
      """ Exam default Choice model """
      id = db.Column(db.Integer, primary_key=True)
      date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      question_id = db.Column(db.Integer, db.ForeignKey('exam_question_model.id'), nullable=False)
      # you can pass a keyword argument of `unique=True` in the below choice_text field
      # that will make it unique across the entire table of choice
      choice_text = db.Column(db.String(100), nullable=False)

      def __str__(self):
        return f"{self.choice_text} of {self.question_id}"

      def __repr__(self):
        return f"{self.choice_text} of {self.question_id}"

*** PLAY WITH API ***
---------------------

Before we move further let us play with the model api. Continuetion from the last tutorial where we stop, when we make debug value to be `True`

From there shutdown the development server and go into the python **shell** ( python interpreter ), make sure you are within that directory you boot up the server by typing **python**, once you are in the interpreter start by importing your **db** and **bcrypt** (for password hash) instance from project package::

  from Schoolsite.config import db, bcrypt

Then also import the models you create for your app in `exam/models.py` and the default User model located in `auth.models.py`::

  from exam.models import ExamQuestionModel, ExamChoiceModel
  from auth.models import User

Next call the `create_all()` method of **db** that will create the tables and database, if it doesn't create db file. Run the below command. But if it create the **default.db** file just ignore::

    db.create_all()

After that let us create two users instance, that will be able to create question and choice of the **ExamQuestionModel** and **ExamChoiceModel** model::

    user1_hashed_pwd = bcrypt.generate_password_hash("12345678").decode('utf-8')
    user1 = User(username="backend-developer", email="developer@backend.com", password=user1_hashed_pwd)

    user2_hashed_pwd = bcrypt.generate_password_hash("12345678").decode('utf-8')
    user2 = User(username="front-developer", email="developer@front.com", password=user2_hashed_pwd)

Now we are to add and commit those users in our database::

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

The next thing now is to start creating our Questions and commit them to our database::

    q1 = ExamQuestionModel(question_text="Is sakyum an extension of flask web framework?", user=user1)
    q2 = ExamQuestionModel(question_text="Is flask better with sakyum", user=user2)

    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

We are to capture our questions `id` (q1 and q2) since they are the once we are going to link to each choice::

    the_q1 = ExamQuestionModel.query.get_or_404(1)
    the_q2 = ExamQuestionModel.query.get_or_404(2)

The choice for our Questions are::

  c1_1 = ExamChoiceModel(choice_text="Yes, it is", question_id=the_q1.id)
  c1_2 = ExamChoiceModel(choice_text="No, it is not", question_id=the_q1.id)
  c1_3 = ExamChoiceModel(choice_text="I don't no", question_id=the_q1.id)

  c2_1 = ExamChoiceModel(choice_text="Yes for sure", question_id=the_q2.id)
  c2_2 = ExamChoiceModel(choice_text="Always the best", question_id=the_q2.id)
  c2_3 = ExamChoiceModel(choice_text="All the time", question_id=the_q2.id)

Commiting choice into database::

    db.session.add(c1_1)
    db.session.add(c1_2)
    db.session.add(c1_3)

    db.session.add(c2_1)
    db.session.add(c2_2)
    db.session.add(c2_3)

    db.session.commit()

To see all questions that we insert into our database::

    ExamQuestionModel.query.all()

To see many other method related to our `ExamQuestionModel.query` by passing it into `dir()` function::

    dir(ExamQuestionModel.query)

We can see choices related to our question number one (1) by::

    ExamQuestionModel.query.get_or_404(1).choices

To see all choices in our database::

    ExamChoiceModel.query.all()

Also like the `ExamQuestionModel.query` we see above, we can see many other method related to our `ExamChoiceModel.query` by passing it into `dir()` function::

    dir(ExamChoiceModel.query)

Lastly let us make a loop over all choices and their questions::

    for i in ExamChoiceModel.query.all():
      i.selector.question_text, i.choice_text

Register our models to admin
----------------------------

In other to register our model, we are to open a sub project folder and open the **config.py** file we see there **(Schoolsite/config.py)**, within create_app function in the file, we are to import our app models (**ExamQuestionModel**, **ExamChoiceModel**) that we want to register, above the method that will create the tables and database **db.create_all()** and we will see a commented prototype above it, then we will append the models in the **reg_models = []** list within **admin_runner** function (inner function of the create_app function). That will register our model in the admin page and we will be able to see it if we vist the admin page

Register model in the form of model view
----------------------------------------

We can register our model in the form of model view by grouping models that are related

To create these model view we have to go into our app admin.py **exam/admin.py**. We will notice some default import::

    from flask_login import current_user
    from flask import redirect, request, url_for
    from flask_admin.contrib.sqla import ModelView

Now below we are to start defining our model view, I will call the model view **QuestionChoiceAdminView** which will look like::

    class QuestionChoiceAdminView(ModelView):
        can_delete = False  # disable model deletion
        can_create = True
        can_edit = True
        page_size = 50  # the number of entries to display on the list view

        # def is_accessible(self):
        #   return current_user.is_authenticated

        # def inaccessible_callback(self, name, **kwargs):
        #   # redirect to login page if user doesn't have access
        #   return redirect(url_for('login', next=request.url))

In other to register our model view, open your sub project folder and open the **config.py** file you see there **(Schoolsite/config.py)**, within create_app function in the file, we are to import our app models (**ExamQuestionModel**, **ExamChoiceModel**) that we want to register and also the model view of our model, above the method that will create the tables and database **db.create_all()**::

    from exam.models import ExamQuestionModel, ExamChoiceModel
    from exam.admin import QuestionChoiceAdminView

and we will see a commented prototype above it, now instead of append it in the **reg_models = []** list within **admin_runner** function (inner function of the create_app function), you are to go below the function we call **adminModelRegister** in (within admin_runner function) and call the admin method called **add_view** and then pass your model view class as an argument, also pass an arguments in the model view class, the first argument is the model class, the second is the **db.session**, and then last give it a category (key word argument) **category="my_models_view". That will register your model in the admin page and you will see it if you vist the admin page::

    admin.add_view(QuestionChoiceAdminView(ExamChoiceModel, db.session, name="Questions", category="Question-Choice"))
    admin.add_view(QuestionChoiceAdminView(ExamQuestionModel, db.session, name="Choices", category="Question-Choice"))

see more documentation on how to write model view class, get look at `Flask-Admin <https://flask-admin.readthedocs.io/en/latest/introduction/#customizing-built-in-views>`_ documentation

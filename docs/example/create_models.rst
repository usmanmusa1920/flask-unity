:tocdepth: 2

App models
##########

Now we are going to create models for our exam app, the models are going to be two `ExamQuestionModel` and `ExamChoiceModel`

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
        return f"{self.question_text}"

      def __repr__(self):
        return f"{self.question_text}"
        
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
        return f"{self.choice_text}"

      def __repr__(self):
        return f"{self.choice_text}"

and save the file

Play with api
-------------

Before we move further let us play with the model api. Continuetion from the last tutorial where we stop, when we make debug value to be `True` ( `last tutorial <https://sakyum.readthedocs.io/en/latest/example/create_app.html>`_ )

From there shutdown the development server and go into the python **shell** ( python interpreter ), make sure you are within that directory you boot up the server by typing **python**, once you are in the interpreter start by importing your **db** and **bcrypt** (for password hash) instance from project package::

  from Schoolsite.config import db, bcrypt

Then also import the models you create for your app in `exam/models.py` and the default User model located in `auth.models.py`::

  from exam.models import ExamQuestionModel, ExamChoiceModel
  from auth.models import User

Next call the `create_all()` method of **db** that will create the tables of our models and database (if it doesn't create db file). Run the below command.::

    db.create_all()

After that let us create two users instance, that will be able to create question and choice of the **ExamQuestionModel** and **ExamChoiceModel** model::

    user1_hashed_pwd = bcrypt.generate_password_hash("12345678").decode('utf-8')
    user1 = User(username="backend-developer", email="developer@backend.com", password=user1_hashed_pwd)

    user2_hashed_pwd = bcrypt.generate_password_hash("12345678").decode('utf-8')
    user2 = User(username="front-developer", email="developer@front.com", password=user2_hashed_pwd)

    user3_hashed_pwd = bcrypt.generate_password_hash("12345678").decode('utf-8')
    user3 = User(username="quantum-developer", email="developer@quantum.com", password=user3_hashed_pwd)

Now we are to add and commit those users in our database::

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

To make sure our users have been added in our database let query the entire User model of our project by::

    User.query.all()

Yes, our users are in the database, good jod. The next thing now is to start creating our Questions and commit them to our database::

    q1 = ExamQuestionModel(question_text="At which year Neil Armstrong landed in the moon?", user=user1)
    q2 = ExamQuestionModel(question_text="What is odd in the choice?", user=user2)
    q3 = ExamQuestionModel(question_text="What is not related to quantum?", user=user3)

    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.commit()

To make sure our `questions` are in the database let query them to see by::

    ExamQuestionModel.query.all()

Yes, our questions are in the database, good jod. We are to capture our questions `id` (q1, q2 and q3) since they are the once we are going to link to each choice::

    the_q1 = ExamQuestionModel.query.get_or_404(1)
    the_q2 = ExamQuestionModel.query.get_or_404(2)
    the_q3 = ExamQuestionModel.query.get_or_404(3)

These are choice for each of our questions, they are::

    # choices for our first question
    c1_1 = ExamChoiceModel(choice_text="In 1969", question_id=the_q1.id)
    c1_2 = ExamChoiceModel(choice_text="In 1996", question_id=the_q1.id)
    c1_3 = ExamChoiceModel(choice_text="In 2023", question_id=the_q1.id)
    c1_4 = ExamChoiceModel(choice_text="In 2007", question_id=the_q1.id)

    # choices for our second question
    c2_1 = ExamChoiceModel(choice_text="python", question_id=the_q2.id)
    c2_2 = ExamChoiceModel(choice_text="java", question_id=the_q2.id)
    c2_3 = ExamChoiceModel(choice_text="linux", question_id=the_q2.id)
    c2_4 = ExamChoiceModel(choice_text="ruby", question_id=the_q2.id)

    # choices for our third question
    c3_1 = ExamChoiceModel(choice_text="qubit", question_id=the_q3.id)
    c3_2 = ExamChoiceModel(choice_text="entanglement", question_id=the_q3.id)
    c3_3 = ExamChoiceModel(choice_text="bit", question_id=the_q3.id)
    c3_4 = ExamChoiceModel(choice_text="superposition", question_id=the_q3.id)

Now let commit the choice into database::

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

To see many other method related to our `ExamQuestionModel.query` by passing it into `dir()` function::

    dir(ExamQuestionModel.query)

To see all choices in our database::

    ExamChoiceModel.query.all()

Also like the `ExamQuestionModel.query` we see above, we can see many other method related to our `ExamChoiceModel.query` by passing it into `dir()` function::

    dir(ExamChoiceModel.query)

Lastly let us make a loop over all question and print each question choices::

    for question in ExamQuestionModel.query.all():
        question
        for choice in question.choices:
            print('\t', f'{choice.id}: ', choice)

Since we insert something into the database, let move on, on how we can make those record to be display in the admin page (by registering the models), because if now we logout from the python interpreter and boot up the server **python thunder.py boot -d True** then navigate to admin page we won't be able to see those models. We can do so below:

Register our models to admin
----------------------------

In other to register our model, we are to open a sub project folder and open the **config.py** file we see there **(Schoolsite/config.py)**, within create_app function in the file, we are to import our app models (**ExamQuestionModel**, **ExamChoiceModel**) that we want to register, above the method that will create the tables **db.create_all()** and we will see a commented prototype above it, then we will append the models in the **reg_models = []** list within **admin_runner** function (inner function of the create_app function). That will register our model in the admin page and we will be able to see it if we vist the admin page now!

Register model in the form of model view
----------------------------------------

We can register our model in the form of model view by grouping models that are related

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

        # def is_accessible(self):
        #   return current_user.is_authenticated

        # def inaccessible_callback(self, name, **kwargs):
        #   # redirect to login page if user doesn't have access
        #   return redirect(url_for('login', next=request.url))

In other to register our model view, open the `config.py` file (Schoolsite/config.py) and import our admin model view (`QuestionChoiceAdminView`) below the import of our `ExamQuestionModel` and `ExamChoiceModel`::

    from exam.models import ExamQuestionModel, ExamChoiceModel
    from exam.admin import QuestionChoiceAdminView

Now comment the **ExamQuestionModel** and **ExamChoiceModel** in the `reg_models` list, go below the function we call **adminModelRegister** in (within admin_runner function) and call the admin method called **add_view** and then pass your model view class as an argument, also pass an arguments in the model view class, the first argument is the model class, the second is the **db.session**, and then last give it a category (key word argument) **category="my_models_view"::

    admin.add_view(QuestionChoiceAdminView(ExamChoiceModel, db.session, name="Questions", category="Question-Choice"))
    admin.add_view(QuestionChoiceAdminView(ExamQuestionModel, db.session, name="Choices", category="Question-Choice"))

That will register your related model in the admin page and you will see them if you vist the admin page::

see more documentation on how to write model view class at `Flask-Admin <https://flask-admin.readthedocs.io/en/latest/introduction/#customizing-built-in-views>`_ documentation

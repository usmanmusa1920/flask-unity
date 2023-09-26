:tocdepth: 2

Connect other flask with flask-unity
####################################

Apparently, there are alot of flask extensions currently, most of which are in `PyPI <https://pypi.org/search/?c=Framework+%3A%3A+Flask>`_, and more are about to exist from different communities of open source. With this **flask-unity** bring tricks on how to connect those other extensions with it.

Same thing with the `docs of flask <https://flask.palletsprojects.com/en/2.3.x/extensions/>`_ on how to connect other extensions, so no big deal.

Wondering on where to put such in your flask project created using flask-unity? Don't worry! We get you!

The place (module) to put such is in your project sub-folder config.py file (<PROJECT_NAME>/<PROJECT_NAME>/config.py), making comparement with our `schoolsite` app it would be **(schoolsite/schoolsite/config.py)**. Import the package at the top, then configure it within the `create_app` function outside the for loop, like so::

    from flask_foo import Foo

    foo = Foo()
    
    def create_app(reg_blueprints=False, conf=Config):
        app = Flask(__name__)
        app.config.from_object(conf)
        app.app_context().push()
        for ext in ext_lst:
            ext.init_app(app)
        foo.init_app(app)
        
**Example using Flask-Mail**

.. code-block:: python
    from flask_mail import Mail

    mail = Mail()
    
    def create_app(reg_blueprints=False, conf=Config):
        app = Flask(__name__)
        app.config.from_object(conf)
        app.app_context().push()
        for ext in ext_lst:
            ext.init_app(app)
        mail.init_app(app)

Next configure it options in your project sub-folder secret.py file (<PROJECT_NAME>/<PROJECT_NAME>/secret.py), within the `Config` class, like::

    MAIL_SERVER : 'smtp.gmail.com'
    MAIL_PORT : 465
    MAIL_USERNAME : developer
    MAIL_PASSWORD : passwd123
    
Next load them within the `load_env` function like::

    os.environ['FLASK_MAIL_SERVER'] = Config.MAIL_SERVER
    os.environ['FLASK_MAIL_PORT'] = Config.MAIL_PORT
    os.environ['FLASK_MAIL_USERNAME'] = Config.MAIL_USERNAME
    os.environ['FLASK_MAIL_PASSWORD'] = Config.MAIL_PASSWORD
    
More docs on how to use flask-mail could be found `here <https://pythonhosted.org/Flask-Mail/>`_

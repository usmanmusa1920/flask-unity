
_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <!-- Hello world HTML index -->
  
  <h1>Welcome to flaskey</h1>
  <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam quidem in iure architecto, iste eius aperiam, ipsam ducimus commodi soluta ea earum quis eveniet illum fugiat voluptatibus voluptatem aspernatur tenetur?</p>
  
</body>
</html>

"""

_css = r"""/* Hello world CSS index */

body {
  padding: 0;
  margin: 0;
}

"""

_js = r"""// Hello world JS index

/* js file */

"""


pro_default_dummy = r"""from flaskey import boot

if __name__ == "__main__":
    boot()
    
# from flaskblog import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)
    
"""


app_default_dummy = r"""from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
  return "Hello world"
  
  
if __name__ == '__main__':
  app.run(debug=True)
"""

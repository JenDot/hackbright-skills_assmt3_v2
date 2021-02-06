from flask import render_template
from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask import Flask, session


app = Flask(__name__)

# This option will cause Jinja to throw UndefinedErrors if a value hasn't
# been defined (so it more closely mimics Python's behavior)
app.jinja_env.undefined = StrictUndefined

# This option will cause Jinja to automatically reload templates if they've been
# changed. This is a resource-intensive operation though, so it should only be
# set while debugging.
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

MOST_LOVED_MELONS = {
    "cren": {
        "img": "http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg",
        "name": "Crenshaw",
        "num_loves": 584,
    },
    "jubi": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg",
        "name": "Jubilee Watermelon",
        "num_loves": 601,
    },
    "sugb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg",
        "name": "Sugar Baby Watermelon",
        "num_loves": 587,
    },
    "texb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg",
        "name": "Texas Golden Watermelon",
        "num_loves": 598,
    },
}

"""In server.py, write a route that serves the template homepage.html at the route /. """


@app.route("/")
def homepage():
    return render_template("homepage.html")


"""At the route /get-name:
    * Get the name that the user submitted (from request.args).
    * Add the user’s name to the session (remember, a session operates very much like a dictionary, so you can add a name
        to the session the same way you would add, for example, the key ‘name’ with the value ‘Balloonicorn’ to a regular Python
        dictionary).
    * After the name has been added to the session, redirect to the /top-melons route.
"""


@app.route("/get-name")
def get_name():
    person = session["person"]
    return redirect("/top-melons")


"""Write a route, /top-melons, that renders the template top-melons.html.
    At the top of server.py, there is a dictionary of 4 melons called MOST_LOVED_MELONS. Those are the melons to display.
    The route /top-melons should render the template top-melons.html and pass through the MOST_LOVED_MELONS dictionary to Jinja.

    At the route /top-melons, check first to see if there is a name stored in the session already. If there is, render the template
    top-melons.html. If there isn’t a ‘name’ key in the session, redirect back to the homepage.
    Similarly, if a user has already entered their name and it’s been stored in the session, we don’t need them to ever see the
    homepage where we ask them for their name again. So, you can update the homepage route at / to check to see if a name is in
    the session, and if so, to redirect to the /top-melons route.
"""


@app.route("/top-melons")
def top_melons():
    if session["person"]:
        return render_template("top-melons.html", melons=MOST_LOVED_MELONS)
    else:
        return redirect("/")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="5000")

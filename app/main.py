from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import FileField, Form, SubmitField
from werkzeug.utils import secure_filename
from app.net import Prediction


app = Flask(__name__)


class HomePage(MethodView):

    d = {0: ['Kawka / Western jackdaw', 'Coloeus monedula'], 1: ['Sroka / Magpie', 'Pica pica'],
         2: ['Gawron / Rook', 'Corvus frugilegus'], 3: ['Sójka / Eurasian jay', 'Garrulus glandarius'],
         4: ['Wrona / Hooded crow', 'Corvus cornix'], 5: ['Kruk / Common raven', 'Corvus corax']}

    def get(self):
        form = PhotoForm()
        return render_template("index.html", form=form, corvid_photo=None, bird=None)

    def post(self):
        form = PhotoForm(request.files)
        file = request.files['file']
        if file:
            try:
                pred = Prediction(file).predict()
                bird = self.d[pred]
                path = f"birds/{bird[0].split('/')[0].strip().lower().replace('ó','o')}.jpg"
            except:
                bird = ["Invalid file", "Please try a different picture"]
                path = None
            return render_template("index.html", form=form, corvid_photo=path, bird=bird)
        else:
            bird = ["No file selected", "Please upload a file"]
            return render_template("index.html", form=form, bird=bird)


class PhotoForm(Form):
    file = FileField("Select a picture")
    submit = SubmitField("Identify")


app.add_url_rule("/", view_func=HomePage.as_view("home"))

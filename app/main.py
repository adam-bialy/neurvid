from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import FileField, Form, SubmitField
from app.net import Prediction
from tensorflow.keras.models import load_model


app = Flask(__name__)

# using model v7-alt
model = load_model("app/nn-final.h5")


class HomePage(MethodView):

    d = {0: ['Kawka / Western jackdaw', 'Coloeus monedula'], 1: ['Sroka / Magpie', 'Pica pica'],
         2: ['Gawron / Rook', 'Corvus frugilegus'], 3: ['Sójka / Eurasian jay', 'Garrulus glandarius'],
         4: ['Wrona / Hooded crow', 'Corvus cornix'], 5: ['Kruk / Common raven', 'Corvus corax']}

    def get(self):
        form = PhotoForm()
        return render_template("index.html", form=form, corvid_photo=None, bird=None)

    # method for returning only one bird
    # def post(self):
    #     form = PhotoForm(request.files)
    #     file = request.files['file']
    #     if file:
    #         try:
    #             pred = Prediction(file).predict()
    #             bird = self.d[pred]
    #             path = f"birds/{bird[0].split('/')[0].strip().lower().replace('ó','o')}.jpg"
    #         except Exception as e:
    #             print(e)
    #             bird = ["Invalid file", "Please try a different picture"]
    #             path = None
    #         return render_template("index.html", form=form, corvid_photo=path, bird=bird)
    #     else:
    #         bird = ["No file selected", "Please upload a file"]
    #         return render_template("index.html", form=form, bird=bird)

    # method for returning only two birds
    def post(self):
        form = PhotoForm(request.files)
        file = request.files['file']
        if file:
            try:
                pred = Prediction(file, model).predict_top2()
                birds = [self.d[i] for i in pred]
                paths = [f"birds/{bird[0].split('/')[0].strip().lower().replace('ó','o')}.jpg" \
                        for bird in birds]
            except Exception as e:
                print(e)
                birds = ["Invalid file", "Please try a different picture"]
                paths = None
            return render_template("index.html", form=form, corvid_photo=paths, bird=birds)
        else:
            bird = ["No file selected", "Please upload a file"]
            return render_template("index.html", form=form, bird=bird)


class PhotoForm(Form):
    file = FileField("Select a picture")
    submit = SubmitField("Identify")


app.add_url_rule("/", view_func=HomePage.as_view("home"))

from flask import Flask, render_template, request
import requests
import flask
import pickle


app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        gre = request.form['GRE Score'].replace(" ", "")
        toefl = request.form['TOEFL Score'].replace(" ", "")
        rank = request.form['University Rating'].replace(" ", "")
        sop = request.form['SOP'].replace(" ", "")
        lor = request.form['LOR'].replace(" ", "")
        cgpa = request.form['CGPA'].replace(" ", "")
        research = request.form['Research'].replace(" ", "")

        gre, toefl, rank, sop, lor, cgpa, research = int(gre), int(toefl), float(rank), float(sop), float(lor), float(cgpa), int(research)

        result = model.predict([[gre, toefl, rank, sop, lor, cgpa, research]])

        return render_template('results.html', result=result)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


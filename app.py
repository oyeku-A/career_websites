from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'A, B',
  'salary': '200'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'B, C',
}, {
  'id': 3,
  'title': 'Data Engineer',
  'location': 'C, D',
  'salary': '300'
}, {
  'id': 4,
  'title': 'Data Specialist',
  'location': 'D, E',
  'salary': '350'
}]


@app.route("/")
def home_page():
  return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def job_opportunities():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

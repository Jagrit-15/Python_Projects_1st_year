from flask import Flask, render_template , redirect , url_for
from flask_bootstrap import Bootstrap5
import csv
import os
from forms import AddingForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/cafes')
def cafes():
    # Build an absolute path relative to main.py's location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'cafe-data.csv')
    with open(csv_path, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/add' , methods=['GET','POST'])
def add():
    form = AddingForm()
    if form.validate_on_submit():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, 'cafe-data.csv')
        with open(csv_path, mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe_name.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

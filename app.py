from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

import logic
from forms import UserInput

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wESWn^!SuGau'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)


# Setting Results Table
class Result(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String(80), nullable=False)
    repo_description = db.Column(db.String(300))
    programing_language = db.Column(db.String(300))
    num_of_open_issues_count = db.Column(db.Integer())
    num_of_pulls_requests = db.Column(db.Integer())

    def __repr__(self):
        return f"Resault(no: '{self.no}', repo name: '{self.repo_name}', repo description: '{self.repo_description}',num_of_open_issues_count: '{self.num_of_open_issues_count}'" \
               f" programing language: '{self.programing_language}'," \
               f" num_of_pulls_requests: '{self.num_of_pulls_requests},)"


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def user_page():
    search_form = UserInput()
    if search_form.validate_on_submit():
        rv = (logic.main(search_form.github_user_name.data, search_form.programing_language.data,
                         search_form.min_num_of_stars.data))
        for ind, value in enumerate(rv):
            ind = Result(repo_name=value[0], repo_description=value[1], programing_language=value[2],
                         num_of_open_issues_count=value[3], num_of_pulls_requests=value[4])
            db.session.add(ind)
            db.session.commit()
    headings = (
        'no', 'Repo name', 'Repo description', 'Programing Language', 'Num of open issues ', 'Num of pulls requests')
    data = db.session.query(Result).order_by(desc(Result.no)).limit(10).all()
    return render_template('home.html', search_form=search_form, headings=headings, data=data)


@app.route('/admin_dashboard')
def admin_dashboard():
    headings = (
        'no', 'Repo name', 'Repo description', 'Programing Language', 'Num of open issues ', 'Num of pulls requests')
    data = Result.query.all()
    return render_template('admin_dashboard.html', headings=headings, data=data)


if __name__ == '__main__':
    app.run(debug=True)

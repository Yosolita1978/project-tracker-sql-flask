from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    rows = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            rows=rows)
    return html

@app.route("/student_search")
def student_search():

    return render_template("student_search.html")

@app.route("/student_add", methods=['GET', 'POST'])
def add_student_info():
    print request.method
    if request.method == 'GET':
        return render_template("student_add.html")
    else:

        student_info = request.form
        first_name = student_info['first_name']
        last_name = student_info['last_name']
        github = student_info['github']

        hackbright.make_new_student(first_name, last_name, github)


        return render_template("post_added_student.html",
                                github=github)

@app.route("/project")
def get_project():


    title = request.args['project']
    rows = hackbright.get_project_by_title(title)
    return render_template("project.html", rows=rows, title=title)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

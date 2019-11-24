from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/instructors")
def main():
    try:
        path = "/Users/sumitoberoi/Documents/SSW-810/HW09/HW12/HW12.db"
        db = sqlite3.connect(path)
    except sqlite3.OperationalError:
        return f"Problem with connecting to {path}"
    else:
        query = """ SELECT instructors.CWID,instructors.Name,instructors.Dept, grades.Course, COUNT(*) as NUM_OF_STUDENTS
                        FROM  instructors JOIN grades on CWID = InstructorCWID
                        Group By instructors.CWID, Course """
        
        row_infos = []
        for row in db.execute(query):
            row_infos.append(row)
        db.close()
        print(row_infos)
        return render_template(
            "instructor.html",
            title="Stevens Repository",
            table_title="Courses and Students Count",
            instructors=row_infos
        )

app.run(debug=True)
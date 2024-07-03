### Code Generation


# main.py
from flask import Flask, render_template, request
import smart_time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    tasks = request.form.getlist('tasks[]')
    time_slots = request.form.getlist('time_slots[]')

    schedule = smart_time.generate_schedule(tasks, time_slots)

    return render_template('schedule.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)


### Code Validation

**Check for variable references in HTML files**

html
<!-- index.html -->
<form action="/generate_schedule" method="POST">
  {% for task in tasks %}
    <input type="text" name="tasks[]" value="{{ task }}">
  {% endfor %}

  {% for time_slot in time_slots %}
    <input type="text" name="time_slots[]" value="{{ time_slot }}">
  {% endfor %}

  <input type="submit" value="Generate Schedule">
</form>

<!-- schedule.html -->
<table>
  {% for task in schedule %}
    <tr>
      <td>{{ task.name }}</td>
      <td>{{ task.start_time }}</td>
      <td>{{ task.end_time }}</td>
    </tr>
  {% endfor %}
</table>


**Corrections if needed**

* None required in this case.

### Output


# main.py
from flask import Flask, render_template, request
import smart_time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', tasks=[], time_slots=[])

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    tasks = request.form.getlist('tasks[]')
    time_slots = request.form.getlist('time_slots[]')

    schedule = smart_time.generate_schedule(tasks, time_slots)

    return render_template('schedule.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)

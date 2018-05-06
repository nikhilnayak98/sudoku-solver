from sudokusolver import *
from flask import Flask, request,  render_template
app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('frontend.html')

@app.route('/solve', methods=['POST'])
def solver():
    complete_string = request.form['cell-0'] + request.form['cell-1'] + request.form['cell-2'] + request.form['cell-3'] + request.form['cell-4'] + request.form['cell-5'] + request.form['cell-6'] + request.form['cell-7'] + request.form['cell-8'] + request.form['cell-9'] + request.form['cell-10'] + request.form['cell-11'] + request.form['cell-12'] + request.form['cell-13'] + request.form['cell-14'] + request.form['cell-15'] + request.form['cell-16'] + request.form['cell-17'] + request.form['cell-18'] + request.form['cell-19'] + request.form['cell-20'] + request.form['cell-21'] + request.form['cell-22'] + request.form['cell-23'] + request.form['cell-24'] + request.form['cell-25'] + request.form['cell-26'] + request.form['cell-27'] + request.form['cell-28'] + request.form['cell-29'] + request.form['cell-30'] + request.form['cell-31'] + request.form['cell-32'] + request.form['cell-33'] + request.form['cell-34'] + request.form['cell-35'] + request.form['cell-36'] + request.form['cell-37'] + request.form['cell-38'] + request.form['cell-39'] + request.form['cell-40'] + request.form['cell-41'] + request.form['cell-42'] + request.form['cell-43'] + request.form['cell-44'] + request.form['cell-45'] + request.form['cell-46'] + request.form['cell-47'] + request.form['cell-48'] + request.form['cell-49'] + request.form['cell-50'] + request.form['cell-51'] + request.form['cell-52'] + request.form['cell-53'] + request.form['cell-54'] + request.form['cell-55'] + request.form['cell-56'] + request.form['cell-57'] + request.form['cell-58'] + request.form['cell-59'] + request.form['cell-60'] + request.form['cell-61'] + request.form['cell-62'] + request.form['cell-63'] + request.form['cell-64'] + request.form['cell-65'] + request.form['cell-66'] + request.form['cell-67'] + request.form['cell-68'] + request.form['cell-69'] + request.form['cell-70'] + request.form['cell-71'] + request.form['cell-72'] + request.form['cell-73'] + request.form['cell-74'] + request.form['cell-75'] + request.form['cell-76'] + request.form['cell-77'] + request.form['cell-78'] + request.form['cell-79'] + request.form['cell-80']
    solve_all([complete_string])
    return complete_string

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
from flask import Flask,render_template,redirect,request

app= Flask(__name__)

@app.route('/')
def name():
		
		return render_template('name.html')

@app.route('/process',methods=['post'])
def my_name():
	print request.form
	name=request.form["name"]

@app.route('/')
def back():

		return redirect('/')

	


app.run(debug=True)
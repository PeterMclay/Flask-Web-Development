from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = '6be82b8fd95bcfbd9e188b0ce964c0e8'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/web_development")
def web_dev():
	return render_template('webdev.html')

@app.route("/mechatronic_design")
def mechatronic_design():
	return render_template('mechatronicdesign.html')

@app.route("/object_oriented_programming")
def object_oriented_programming():
	return render_template('objprogramming.html')

if __name__ == '__main__':
	app.run(debug=True)
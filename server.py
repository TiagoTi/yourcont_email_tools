from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/welcome_to_your_cont', methods=['GET', 'POST'])
def welcome_to_your_cont():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('welcome_to_your_cont.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

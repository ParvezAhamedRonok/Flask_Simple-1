from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your own secret key

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'count' not in session:
        session['count'] = 0

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'increment':
            session['count'] += 1
        elif action == 'decrement':
            session['count'] -= 1

    return render_template('index.html', count=session['count'])

if __name__ == '__main__':
    app.run(debug=True)

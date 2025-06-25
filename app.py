from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

questions = [
    {'que': 'Which is the largest country?', 'ans': ['Russia', 'India', 'USA', 'China'], 'cans': 'Russia'},
    {'que': 'Which is the largest continent?', 'ans': ['Asia', 'Africa', 'Europe', 'South America'], 'cans': 'Asia'},
    {'que': 'Which is the capital of India?', 'ans': ['New Delhi', 'Lucknow', 'Mumbai', 'Kolkata'], 'cans': 'New Delhi'},
    {'que': 'Which team won IPL 2025?', 'ans': ['RCB', 'CSK', 'KKR', 'KXIP'], 'cans': 'RCB'},
    {'que': 'Who won the Nations League 2025?', 'ans': ['Portugal', 'Spain', 'France', 'Germany'], 'cans': 'Portugal'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start', methods=['POST'])
def start():
    session['username'] = request.form['username']
    session['score'] = 0
    session['q_index'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        selected = request.form.get('answer')
        index = session['q_index']
        if selected and selected == questions[index]['cans']:
            session['score'] += 1
        session['q_index'] += 1

    if session['q_index'] < len(questions):
        q = questions[session['q_index']]
        return render_template('quiz.html', q=q, qn=session['q_index']+1, total=len(questions))
    else:
        return redirect(url_for('result'))

@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(questions)
    return render_template('result.html', score=score, total=total, username=session.get('username'))

@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

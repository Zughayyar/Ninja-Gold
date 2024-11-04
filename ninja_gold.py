from flask import Flask, render_template, session, request, redirect
from random import randrange

app = Flask(__name__)  
app.secret_key = "keep it safe"

@app.route('/')
def index():
    if 'score' not in session:
        session['score'] = 0
        session['message'] = []
    return render_template("index.html")
    
@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        rand_farm = randrange(10,20,1)
        session['score'] += rand_farm
        session['message'].insert(0,f'Earned {rand_farm} golds from the farm!')
    
    if request.form['building'] == 'cave':
        rand_cave = randrange(5,10,1)
        session['score'] += rand_cave
        session['message'].insert(0,f'Earned {rand_cave} golds from the cave!')
    
    if request.form['building'] == 'house':
        rand_house = randrange(2,5,1)
        session['score'] += rand_house
        session['message'].insert(0,f'Earned {rand_house} golds from the house!')
    
    if request.form['building'] == 'casino':
        session['rand_casino'] = randrange(-50,50,1)
        session['score'] += session['rand_casino']
        session['message'].insert(0,f'Earned {session['rand_casino']} golds from the casino!')
    
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session['score'] = 0
    session['message'] = []
    return redirect('/')
   

if __name__=="__main__":   
    app.run(debug=True)    
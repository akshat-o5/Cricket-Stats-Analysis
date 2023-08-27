from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def analytics():
    return render_template('analytics.html')


@app.route('/submit1', methods=['POST'])
def status():
    return render_template('status.html')



@app.route('/submit2', methods=['POST'])
def won():
    return render_template('matches_won.html')



@app.route('/submit3', methods=['POST'])
def innings():
    return render_template('innings.html')



@app.route('/submit4', methods=['POST'])
def ground():
    return render_template('ground_type.html')   



@app.route('/submit5', methods=['POST'])
def opposition():
    return render_template('opposition_teams.html')   



@app.route('/submit6', methods=['POST'])
def venue():
    return render_template('venue.html')   



@app.route('/submit7', methods=['POST'])
def year():
    return render_template('year.html')   



@app.route('/submit8', methods=['POST'])
def position():
    return render_template('position.html') 



if __name__ == "__main__":
    # app = create_app()
    app.run(debug=True)
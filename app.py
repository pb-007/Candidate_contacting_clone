from flask import Flask, render_template, request
from candidate import Candidate

app = Flask(__name__)


candidates = [
        Candidate("A", ["B", "C", "J"]),
        Candidate("D", ["E", "F", "G"]),
        Candidate("H", ["I", "K", "V"]),
        Candidate("J", ["V"]),
        Candidate("K", ["L", "M", "N", "A"]),
        Candidate("O", ["P", "V", "U"]),
        Candidate("Q", ["S", "T", "D"]),
        Candidate("U", ["H", "J"]),
        Candidate("V", ["W", "X", "Y", "Z"])
    ]

@app.route('/')
def index():
    return render_template('index.html', candidates=candidates)

@app.route('/contact_friends', methods=['POST'])
def contact_friends():
    selected_candidates = request.form.getlist('candidate')
    contacted_friends = []

    for candidate_name in selected_candidates:
        candidate = next((c for c in candidates if c.name == candidate_name), None)
        if candidate:
            for friend_name in candidate.classmates:
                if friend_name not in selected_candidates and friend_name not in contacted_friends:
                    contacted_friends.append(friend_name)

    return render_template('contacted_friends.html', contacted_friends=contacted_friends)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
import scripts.rand_tweet as nba_twitter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html", tweet = nba_twitter.random_tweet())


if __name__ == '__main__':
    app.run(debug=True)
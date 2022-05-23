from flask import Flask, render_template
import scripts.tweepy_data as nba_twitter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

print(nba_twitter.randomNBAPlayer())

if __name__ == '__main__':
    app.run(debug=True)
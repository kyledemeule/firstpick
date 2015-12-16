from flask import Flask, render_template, request, redirect, url_for, abort
import lib.picker as picker
import util
application = Flask(__name__)

REVIEW_PAGE_LENGTH = 10

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/roster", methods=['POST'])
def roster():
    players = util.parse_params(request.form)
    teams = picker.pick_teams(players)
    if teams:
        return render_template('roster.html', teams=teams)
    else:
        abort(500)

if __name__ == "__main__":
    application.run(debug=True)
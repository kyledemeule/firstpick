from flask import Flask, render_template, request, redirect, url_for, abort
application = Flask(__name__)

REVIEW_PAGE_LENGTH = 10

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/roster")
def roster():
    search_type = request.args.get('search_type').strip()
    search_term = request.args.get('search_term').strip()
    if search_type == "team":
        return redirect(url_for('product', asin=search_term))
    else:
        # include a message
        redirect(url_for('index'))

if __name__ == "__main__":
    application.run(debug=True)
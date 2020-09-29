from Response import Response
from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)

error_to_get_response = "Failed to make request by this url"
error_to_parse_content = "Failed to read response from server"
error_status_code = "Couldn't get the authorization token"


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/nbu')
def main():
    res = Response()
    response = res.get_response()
    if response is None:
        return return_error(error_to_get_response)

    if response.status_code != 200:
        return return_error(error_status_code)

    json_result = res.parse_content(response.content)
    if json_result is None:
        return return_error(error_to_parse_content)

    return render_template("index.html", model=json_result, date=show_date())


def return_error(error):
    return render_template("index.html", error=error)


def show_date():
    date = datetime.date.today()
    return date.strftime("%d/%m/%Y\n")

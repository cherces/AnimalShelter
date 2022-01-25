from flask import Blueprint, render_template, request, redirect, url_for, make_response
from flask_login import login_required
import pdfkit


news_b = Blueprint('news_b', __name__)


@news_b.route('/news')
@login_required
def index():
    return render_template("news.html")


@news_b.route('/news', methods=["POST"])
@login_required
def news():
    if request.form['operation'] == "print":
        return redirect(url_for("news_b.print_new", text=request.form['text']))

    return render_template('news.html')


@news_b.route('/news/print')
@login_required
def print_new():
    text = request.args.get('text')

    html = render_template("pdf_template.html", text=text)

    config = pdfkit.configuration(wkhtmltopdf="lib\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    pdf = pdfkit.from_string(html, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

    return response
    #return render_template('news.html')


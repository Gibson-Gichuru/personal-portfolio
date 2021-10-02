from flask import render_template

from . import main


@main.route('/')
def home():

    return render_template('/main/index.html')



@main.route('/project/details')
def project_details():

    return render_template('/main/project_details.html')
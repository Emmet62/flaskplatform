from flask import render_template
from app import app

from systeminfo.systeminfo import get_platform_info


@app.route('/')
def index():
	returnDict = {}
	returnDict['user'] = 'Emmet Tracey'
	returnDict['title'] = 'Home'
	returnDict['platform'] = get_platform_info()
	return render_template("index.html", **returnDict)


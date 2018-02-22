from flask import render_template
from app import app
from systeminfo import systeminfo


@app.route('/')
def index():
	returnDict = {}
	returnDict['user'] = 'Emmet the Dark and Terrible'
	returnDict['title'] = 'Home'
	returnDict['platform'] = systeminfo.get_platform_info()
	return render_template("index.html", **returnDict)


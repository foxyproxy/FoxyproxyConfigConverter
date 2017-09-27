import foxyconvert
from flask import render_template, make_response, request
from app import app

@app.route('/', methods = ['GET', 'POST'])  #@app.route('/')
def index():
    UA = {}
    UA['os'] = request.user_agent.platform
    UA['path'] = {'macos': '/Users/<i>&lt;YOUR_USERNAME&gt;</i>/Library/Application Support/Firefox/Profiles/<i>&lt;YOUR_PROFILE&gt;</i>/<b><i>foxyproxy.xml</i></b>',
                  'linux': '/home/<i>&lt;YOUR_USERNAME&gt;</i>/.mozilla/firefox/<i>&lt;YOUR_PROFILE&gt;</i>/<b><i>foxyproxy.xml</i></b>',
                  'windows': r'C:\Users\<i>&lt;YOUR_USERNAME&gt;</i>\AppData\Roaming\Mozilla\Firefox\Profiles\<i>&lt;YOUR_PROFILE&gt;</i>\\<b><i>foxyproxy.xml</i></b>'}
    if request.method == 'GET':
        # Set the shortened version of the UA
        return render_template("index.html", upload_file = False, UA = UA)
    else:
        file = request.files['oldConfData']
        if not file:
            result = False
        else:
            file_contents = file.stream.read()
            # Make sure it's an XML file matching our spec.
            if not file_contents.startswith('<?xml version="1.0" encoding="UTF-8"?>\n<foxyproxy'):
                result = False
            else:
                result = foxyconvert.main(file_contents)
                #result = transform(file_contents)  # this is the Business-End
        response = make_response(render_template("index.html", upload_file = result, UA = UA))
        #response.headers["Content-Disposition"] = "attachment; filename=foxyproxy.json"  # if we want to make it downloadable instead?
        return response

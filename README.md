# FoxyProxy Plugin Configuration Converter
If you're reading this, it's likely that you want to run a local instance of the configuration converter. This is encouraged and advisable; while I can personally guarantee that we don't keep what you upload (nor would we need or want to) on [our online instance](https://getfoxyproxy.org/configconverter), we released this tool under an open source license so that you can run it locally and modify it as you see fit. We even include a commandline tool you can use so you don't even need to host the website interface! (Which is a good thing; uwsgi is not for the faint of heart.)

## Usage
The quickest way to get started is to make sure **Python 2.6+** is installed at the bare minimum. The web interface (**app/{views, models, etc.}.py**) and commandline interface (**app/fpconvert-cli.py**) have both been tested with Python 3, and both work just fine.

It's highly recommended that you install the [LXML](http://lxml.de/) module as well; it offers much safer processing. Since you're only processing one configuration file and it's (presumably) your own, though, this isn't as much of a concern; it'll work just fine with the Python standard library modules.

### Commandline Interface
To use the tool from the commandline, simply execute the **app/fpconvert-cli.py** application - it only takes one (required) argument, the path to your **foxyproxy.xml** file. See [our online instance](https://getfoxyproxy.org/configconverter) for more info on where to find that file; it should be in the base of your Firefox profile directory. It has been tested and works in GNU/Linux, macOS, and Windows 10.

Note that if you wish to use Python 3, you must execute it as follows (according to what the binary is called on your system):

```
python3 fpconvert-cli.py path/to/foxyproxy.xml
```

### Web Interface
The web interface is written in [Flask](http://flask.pocoo.org/). You'll need to have the module installed for the version of Python you want to use. To run a local instance, simply run:

```
FLASK_APP=run.py flask run
```

in the root directory of the project. If you want something more persistent, however, you'll need to use something like [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/). Unfortunately, that's a major undertaking that's out-of-scope for this documentation. The web interface, both Flask execution and uwsgi deployment, has only been tested in GNU/Linux.
from eve import Eve
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from eve.render import send_response
from eve_docs.config import get_cfg


app = Eve(__name__)
Bootstrap(app)


@app.route('/ui')
def ui():
    return render_template('ui.html')


# Unfortunately, eve_docs doesn't support CORS (too bad!), so we had to reimplement it ourselves
@app.route('/docs/spec.json')
def specs():
    return send_response(None, [get_cfg()])

if __name__ == '__main__':
    app.run(debug=True)
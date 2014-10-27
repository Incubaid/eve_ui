from eve import Eve
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

app = Eve(__name__)
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')

@app.route('/ui')
def ui():
    return render_template('ui.html')

if __name__ == '__main__':
    app.run(debug=True)
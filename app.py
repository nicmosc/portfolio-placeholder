from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
app.config['DEBUG'] = True

assets = Environment(app)
less = Bundle('styles/app.less', filters='less',depends='styles/less/**/*.less', output='app.css')
assets.register('less', less)

@app.route('/')
def index():
  return render_template('index.html')


# @app.route('/_add_numbers')
# def addNumbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#
#     initRequest = requests.post("http://nlp.stanford.edu:8080/parser/index.jsp",
#                                 timeout=1)  # test if the parser is still at this address
#     status_code = initRequest.status_code
#     print status_code
#
#     return jsonify(result=a + b)

if __name__ == '__main__':
  app.run(debug=True)

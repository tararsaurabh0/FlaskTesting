from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

@app.route('/test')
def function():
  print("Function invoked through Webhook")
  return "<h1>You are going to Wins</h1>"
app.run(host='0.0.0.0', port=8080)
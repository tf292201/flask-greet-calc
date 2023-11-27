from flask import Flask, request

from operations import add, sub, mult, div  

app = Flask(__name__)

@app.route('/add')
def add_rt():
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = add(a, b)
  return str(result)


@app.route('/subtract')
def subtract_rt():
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = sub(a, b)
  return str(result)

@app.route('/multiply')
def multiply_rt():
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = mult(a, b)
  return str(result)

@app.route('/divide')
def divide_rt():
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  result = div(a, b)
  return str(result)

@app.route('/math/<op>')
def math_rt():
  a = int(request.args.get('a'))
  b = int(request.args.get('b'))
  operation = request.args.get('op')

  operations = {
    'add': add,
    'subtract': sub,
    'multiply': mult,
    'divide': div
  }

  if operation in operations:
    result = operations[operation](a, b)
  else:
    return 'Invalid operation'

  return str(result)

if __name__ == '__main__':
  app.run()

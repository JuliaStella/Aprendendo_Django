from bottle import jinja2_view,route, run, request

@route('/<area>')
@jinja2_view('')

def teste()

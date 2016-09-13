from pyramid.response import Response
from pyramid.view import view_config




@view_config(route_name='home', renderer='../templates/index.jinja2')
def form_view(request):
    return {'a':1}

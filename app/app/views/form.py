from pyramid.view import view_config
from ..models import Category, Partner
import transaction


@view_config(route_name='home', renderer='templates/index.jinja2')
def form_view(request):
    querry = request.dbsession.query(Category).all()
    return {'a': querry}


@view_config(route_name='signup',
             renderer='templates/index.jinja2',
             request_method='POST')
def signup(request):
    partner = Partner(
        name=request.POST.get('name'),
        email=request.POST.get('email'),
    )

    with transaction.manager:
        request.dbsession.add(partner)

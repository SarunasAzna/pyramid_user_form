from pyramid.view import view_config
from ..models import Category, Partner
import transaction


@view_config(route_name='home', renderer='templates/index.jinja2')
def form_view(request):
    querry = request.dbsession.query(Category).all()
    return {'a': querry}


@view_config(route_name='review', request_method="GET", renderer='templates/list.jinja2')
def list_view(request):
    querry = request.dbsession.query(Partner).all()
    return {'records': querry}

@view_config(route_name='signup',
             renderer='templates/OK.jinja2',
             request_method='POST')
def signup(request):
    categ_names = []
    data = request.POST
    for k, v in data.iteritems():
        if k == 'category_ids':
            categ_names.append(v)
    categs = request.dbsession.query(Category).filter(
        Category.name.in_(categ_names)
    ).all()
    partner = Partner(
        name=data.get('name'),
        email=data.get('email'),
        category_ids=categs
    )

    with transaction.manager:
        request.dbsession.add(partner)
    return {}

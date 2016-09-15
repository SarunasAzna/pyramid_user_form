from pyramid.response import Response
from pyramid.view import view_config
from ..models import Category, Partner
import transaction
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)
from sqlalchemy.ext.declarative import declarative_base  # noqa
from sqlalchemy.orm import relationship, backref  # noqa
from sqlalchemy.orm import (  # noqa
                                scoped_session,
                                sessionmaker,
                                )

from zope.sqlalchemy import ZopeTransactionExtension  # noqa

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()




@view_config(route_name='home', renderer='templates/index.jinja2')
def form_view(request):
    querry = request.dbsession.query(Category).all()
    return {'a':querry}

@view_config(route_name='signup',
             renderer='templates/index.pt',
             request_method='POST')
def signup(request):
    l = Partner(
        name=request.POST.get('name'),
        email=request.POST.get('email'),
    )

    with transaction.manager:
        DBSession.add(l)


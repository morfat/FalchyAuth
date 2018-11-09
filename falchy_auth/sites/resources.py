
import falcon

from .models import Site
from .serializers import *

from falchy.core.resources import ListCreateResource ,RetrieveUpdateResource


class ListCreateSites(ListCreateResource):

    login_required = True
    model = Site
    serializer_class = SiteSerializer


class RetrieveUpdateSite(RetrieveUpdateResource):
    login_required = False

    model = Site

    serializer_class = SiteSerializer




import falcon

from .models import Tenant
from .serializers import *

from falchy.core.resources import ListCreateResource ,RetrieveUpdateResource





class ListCreateTenants(ListCreateResource):

    login_required = True
    multitenant = False #doesnot have tenant_id field
    
    model = Tenant

    filterable_fields = ('application_id',)
    searchable_fields = ('name',)

    serializer_class = TenantSerializer

    def get_queryset(self,req,**kwargs):
        application_id = self.get_authenticated_application(req).get("id")

        return self.model.all().where( self.model.application_id == application_id )



class RetrieveUpdateTenant(RetrieveUpdateResource):
    login_required = True

    model = Tenant

    serializer_class = TenantSerializer

    def get_queryset(self,req,**kwargs):
        application_id = self.get_authenticated_application(req).get("id")

        return self.model.all().where( self.model.application_id == application_id )




    
   

        




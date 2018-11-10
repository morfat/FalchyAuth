
import falcon

from .models import Client
from .serializers import ClientSerializer, GenerateClientSecretSerializer

from falchy.core.resources import ListCreateResource ,RetrieveUpdateResource, CreateResource

class ClientMixin:

    def get_client(self, client_id):
        if not client_id:
            raise falcon.HTTPBadRequest(title="Missing client_id Field", description="client_id field is needed")
        
        client =  db.objects( Client.get(client_id) ).fetch()[0]
        if not client:
            raise falcon.HTTPBadRequest(title="Invalid Client", description="Valid client_id is needed")
        
        return client


class GenerateClientSecret(CreateResource):
    model = Client
    serializer_class = GenerateClientSecretSerializer

    def create(self,req,resp,db,posted_data, **kwargs):
        # print ( posted_data )
        pk = posted_data.get("id")
        data = {"client_secret": posted_data.get("client_secret") }
        qset = db.objects( self.model.update() ).filter( id__eq=pk )

        if self.multitenant:
            qset = qset.filter( tenant_id__eq=self.get_auth_tenant_id(req) )
        
        #save
        qset.update(**data)

        return self.get_object(req,db,pk)




class ListCreateClients(ListCreateResource):

    login_required = True
  
    model = Client

    filterable_fields = ('organization_id',)
    searchable_fields = ('name',)

    serializer_class = ClientSerializer


class RetrieveUpdateClient(RetrieveUpdateResource):
    login_required = True

    model = Client

    serializer_class = ClientSerializer


    


    
   

        






from .models import Permission
from .serializers import PermissionSerializer

from falchy.core.resources import ListCreateResource ,RetrieveUpdateResource
from sqlalchemy import select
from ..content_types.models import ContentType

class ListCreatePermissions(ListCreateResource):

    login_required = True

    multitenant = False
  
    model = Permission

    serializer_class = PermissionSerializer
    filterable_fields = ('content_type_id',)

    def get_queryset(self,req,**kwargs):
        queryset = select( [ ContentType.display_name.label('content_type_display_name'),
                         ContentType.code_name.label('content_type_code_name'),
                         Permission.id, Permission.display_name, Permission.code_name,
                         Permission.content_type_id 
                        ] 
            ).select_from( Permission.__table__.join(
                ContentType, ContentType.id == Permission.content_type_id )
            ).where( ContentType.application_id == application_id )



        return queryset #self.model.all().where( self.model.application_id == application_id )


    


class RetrieveUpdatePermission(RetrieveUpdateResource):
    login_required = True
    multitenant = False

    model = Permission

    serializer_class = PermissionSerializer


    


    
   

        




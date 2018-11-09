

import serpy
from falchy.core.serializers import BaseSerializer

class PermissionSerializer(BaseSerializer):
    code_name = serpy.StrField()
    display_name = serpy.StrField()
    content_type_id = serpy.StrField(required=False)
   

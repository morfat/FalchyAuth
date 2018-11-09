
import json
import serpy
from falchy.core.serializers import BaseSerializer

class ContentTypeSerializer(BaseSerializer):
    code_name = serpy.StrField()
    display_name = serpy.StrField()
    application_id = serpy.StrField(required=False)
   

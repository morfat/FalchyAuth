

import serpy
from falchy.core.serializers import BaseSerializer
from jwcrypto import jwk
import json

class TenantSerializer(BaseSerializer):
    
    name = serpy.StrField()
    is_super_tenant = serpy.BoolField()
    application_id = serpy.StrField()
    #host_name = serpy.StrField()
    business_mode = serpy.StrField()  #B2B or B2C
    auth_username_field = serpy.StrField(required=False)
   

    
  




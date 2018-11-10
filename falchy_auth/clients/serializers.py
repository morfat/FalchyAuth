
import json
import serpy
from falchy.core.serializers import BaseSerializer
from jwcrypto import jwk

class ClientSerializer(BaseSerializer):

    name = serpy.StrField()
    #is_first_party = serpy.BoolField()
    client_type = serpy.MethodField()
    #auth_call_back_urls = serpy.StrField(required=False)
    web_origins =  serpy.StrField(required=False)
    #client_secret = serpy.MethodField()
    client_id = serpy.StrField(required=False)
    description =  serpy.StrField(required=False)
    organization_id = serpy.StrField()
    is_active = serpy.BoolField()
    #tenant_id = serpy.StrField()
    #is_confidential = serpy.BoolField( required=False)

    def get_client_type(self,obj):
        return 'backend'


    

    class Meta:
        read_protected_fields = ('client_secret',)
        write_protected_fields = ('client_id','id','is_confidential','created_at','updated_at',)

class GenerateClientSecretSerializer(BaseSerializer):
    client_secret = serpy.MethodField()
    client_id = serpy.StrField()

    class Meta:
        read_protected_fields = ()
        write_protected_fields = ()

    def get_client_secret(self,obj):
        client_type = obj.get("client_type")
        client_secret = obj.get("client_secret")
        if client_type == 'spa':
            return None
        
        if client_secret:
            return client_secret
        key = jwk.JWK.generate(kty = 'oct',size = 256)
        return json.loads(key.export()).get("k")
   




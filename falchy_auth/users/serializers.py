

import serpy
from falchemy_rest.serializers import BaseSerializer

class UserSerializer(BaseSerializer):
 
    organization_id = serpy.StrField(required=False) #when given , we assume we are adding another organization member.
    email =  serpy.StrField(required = False)
    phone_number =  serpy.StrField(required = False)

    first_name =  serpy.StrField(required = False)
    last_name =  serpy.StrField(required = False) 

    email_is_confirmed =  serpy.BoolField(required = False) 
    phone_number_is_confirmed =  serpy.BoolField(required = False) 
    is_active =  serpy.BoolField(required = False) 
    is_staff =  serpy.BoolField(required = False) 
    is_super_user =  serpy.BoolField(required = False) 
    full_name = serpy.MethodField()

    def get_full_name(self, obj):
        return "%s %s" %( obj.get("first_name"), obj.get("last_name") )


  
    class Meta:

        read_protected_fields = ('password',)
        write_protected_fields = ('full_name',)



class UserRegisterSerializer(BaseSerializer):
    host_name = serpy.StrField() # the domain and port of the tenant
    #client_id = serpy.StrField(required=False)
    organization_name = serpy.StrField(required=False) #needed for  for B2B tenant business mode type.

    email =  serpy.StrField(required = False)
    phone_number =  serpy.StrField(required = False)
    password =  serpy.StrField(required = False)

    first_name =  serpy.StrField(required = False)
    last_name =  serpy.StrField(required = False) 
 
    class Meta:

        read_protected_fields = ('password',)
        write_protected_fields = ()





class LoginUserSerializer(BaseSerializer):

    """ for use in getting access token"""

    host_name = serpy.StrField() # the domain and port of the tenant
    email =  serpy.StrField(required = False)
    phone_number =  serpy.StrField(required = False)
    password = serpy.StrField()


    
class UserChangePasswordSerializer(BaseSerializer):
    current_password = serpy.StrField()
    new_password = serpy.StrField()


class UserResetPasswordSerializer(BaseSerializer):
    host_name = serpy.StrField() # the domain and port of the tenant
    email =  serpy.StrField(required = False)
    phone_number =  serpy.StrField(required = False)
    #client_id = serpy.StrField()



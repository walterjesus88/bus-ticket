"""User permission"""
from rest_framework.permissions import BasePermission

class IsAccountOwner(BasePermission):
    def has_object_permissions(self,request,view,obj):
        """Check obj and user are the same."""
        print(self.user)
        print(obj)
        #import pdb; pdb.set_trace()
        return request.user==obj


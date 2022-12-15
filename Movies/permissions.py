from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' :
            return True
        if  request.user==obj.publisher:
            return True
        else:
            return False  

class IsdetailFromGenre(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' :
            if  request.user==obj.publisher:
                return True
        else:
            return False  
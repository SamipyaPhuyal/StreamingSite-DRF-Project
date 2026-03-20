from rest_framework import permissions
class UserReReview(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ["PUT","PATCH","DELETE"]:
            if (obj.author==request.user) or request.user.is_staff:
                return True
        return False
    
class WatchListMod(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ["POST","PUT","PATCH","DELETE"]:
            if request.user and request.user.is_staff:
                return True
        return False
    
class streamMod(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ["POST","PUT","PATCH","DELETE"]:
            if request.user and request.user.is_staff:
                return True
        return False
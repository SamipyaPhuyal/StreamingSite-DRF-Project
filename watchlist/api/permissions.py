from rest_framework import permissions
class UserReReview(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ["PUT","PATCH","DELETE"]:
            if obj.author==request.user:
                return True
        return False

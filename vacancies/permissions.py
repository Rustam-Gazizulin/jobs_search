from rest_framework.permissions import BasePermission

from users.models import User


class VacancyCreatePermission(BasePermission):
    message = 'Добавлять вакансии может только Кадровик'

    def has_permission(self, request, view):
        if request.user.role == User.HR:
            return True
        return False

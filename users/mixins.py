from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class LoggedOutOnlyView(UserPassesTestMixin):
    
    permission_denied_message = "Page not found"

    def test_func(self):  # test_func()이 true라면 다음 것으로 넘어갈 수 있음
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("core:home")
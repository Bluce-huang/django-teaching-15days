from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from backweb.models import User


class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):

        path = request.path
        if path == '/backweb/my_login/':
            return None

        session_id = request.COOKIES.get('session_id')
        # cookie中没有session_id值，说明用户根本没登录
        if not session_id:
            return HttpResponseRedirect(reverse('backweb:my_login'))

        user = User.objects.filter(session_id=session_id)
        # 服务端验证
        if not user:
            return HttpResponseRedirect(reverse('backweb:my_login'))

        # 可以不用返回或则返回None
        return None

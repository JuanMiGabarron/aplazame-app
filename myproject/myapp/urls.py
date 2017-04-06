from django.conf.urls import url
from myapp.views import index, new_curso, curso
from myapp.views import sign_in, sign_out, create_user, login_user

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signin', sign_in, name='sign_in'),
    url(r'^signout', sign_out, name='sign_out'),
    url(r'^createuser', create_user, name='createuser'),
    url(r'^loginuser', login_user, name='loginuser'),
    url(r'^new_curso', new_curso, name='new_curso'),
    url(r'^curso/(?P<curso>\w+)/', curso, name='curso'),
]

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from accounts.views import SignUpView
from users import views as user_views
from message import views as message_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from categorys import views as category_views


urlpatterns = [
    path('', include('categorys.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('users.urls')),
    # path('categorys/', include('categorys.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', category_views.PageListView.as_view(), name='index_all'),
    #following path is for comments
    # path(r'comments/', include('django_comments_xtd.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('user/', include('users.urls')),
    path('messages/', include('message.urls')),
    # path(r'^messages/', include('django_messages.urls')),


]

"""VVV If we have issues with deployment, this is probably why VVV"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
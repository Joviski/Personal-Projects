from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('snippets/', views.snippet_list, name= 'snippet-list'),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    #path('token/gen/',views.tokengen),
    path('api-token-auth/', obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)

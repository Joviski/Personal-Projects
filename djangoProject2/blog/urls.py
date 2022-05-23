from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    #post views
    #path('',post_list, name='post_list'), #FBV
    path('<int:post_id>/share/',post_share,name='post_share'),
    path('', PostListView.as_view(), name='post_list'),  # CBV

    #path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
    path('<int:id>/', post_detail, name='post_detail')

]
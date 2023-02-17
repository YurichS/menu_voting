from django.urls import path
from .views import MenuListView, MenuUploadView, VoteView, ResultView
urlpatterns = [
    path('menu_list/', MenuListView.as_view()),
    path('menu_upload/', MenuUploadView.as_view()),
    path('vote/<int:menu_id>/', VoteView.as_view()),
    path('result/', ResultView.as_view())
]
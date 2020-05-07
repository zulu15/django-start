from django.urls import path,include
from boards import views

#app_name = 'boards'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_poll/', views.create_poll, name='create'),
	path('<int:pk>/delete/', views.DeletePollView.as_view(), name='delete'),

]
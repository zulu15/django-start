from django.urls import path,include
from boards import views


urlpatterns = [
 	

 	# ex: /boards/
    path('', views.index, name='index'),
 
    # ex: /boards/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /boards/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /boards/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
from django.urls import path
from course import views

app_name = 'course'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('add-course/', views.add_course, name='add_course'),
    path('add-article/', views.add_article, name='add_article'),
    path('update-article/', views.update_article, name='update_article'),
    path('delete-article/', views.delete_article, name='delete_article'),

    path('add-article-logic/', views.add_article_logic, name='add_article_logic'),
    path('update-article-logic/', views.update_article_logic, name='update_article_logic'),
    path('add-course-logic/', views.add_course_logic, name='add_course_logic'),
    path('get-sub-categories/', views.get_sub_categories, name='get_sub_categories'),
]


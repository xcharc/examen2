from django.urls import path
from . import views
urlpatterns = [
    path('ids/', views.list_ids, name='list_ids'),
    path('ids-titles/', views.list_ids_titles, name='list_ids_titles'),
    path('unresolved/', views.list_unresolved, name='list_unresolved'),
    path('resolved/', views.list_resolved, name='list_resolved'),
    path('ids-user/', views.list_ids_user, name='list_ids_user'),
    path('resolved-user/', views.list_resolved_user, name='list_resolved_user'),
    path('unresolved-user/', views.list_unresolved_user, name='list_unresolved_user'),

    # CRUD URLs
    path('', views.PendingTaskListView.as_view(), name='pendingtask_list'),
    path('create/', views.PendingTaskCreateView.as_view(), name='create_task'),
    path('edit/<int:pk>/', views.PendingTaskUpdateView.as_view(), name='edit_task'),
    path('delete/<int:pk>/', views.PendingTaskDeleteView.as_view(), name='delete_task'),

    path('ids/', views.list_ids, name='list_ids'),
]
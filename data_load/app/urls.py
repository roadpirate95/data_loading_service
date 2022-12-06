from django.urls import path
from app.views import CreateEmployeeView, home, EmployeeListView, EmployeeDeleteView, EmployeeUpdateView


app_urlpatterns = [
    path('', home, name='home'),
    path('create/', CreateEmployeeView.as_view(), name='create_employee'),
    path('all/', EmployeeListView.as_view(), name='list_employee'),
    path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
]

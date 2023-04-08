from django.urls import path
from .views import CompanyList, CompanyDetail, EmployeeList, EmployeeDetail, DeviceList, DeviceDetail, AssetList, AssetDetail

urlpatterns = [
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetail.as_view()),
    path('employees/', EmployeeList.as_view()),
    path('employees/<int:pk>/', EmployeeDetail.as_view()),
    path('devices/', DeviceList.as_view()),
    path('devices/<int:pk>/', DeviceDetail.as_view()),
    path('assets/', AssetList.as_view()),
    path('assets/<int:pk>/', AssetDetail.as_view()),
]

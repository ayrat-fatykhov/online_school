from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView, \
    PaymentDestroyAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/view/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_view'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_delete'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

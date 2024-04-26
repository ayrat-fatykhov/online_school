from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentCreateAPIView(CreateAPIView):

    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payed_course', 'pay_approach']
    ordering_fields = ['date']


class PaymentRetrieveAPIView(RetrieveAPIView):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(UpdateAPIView):

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(DestroyAPIView):

    queryset = Payment.objects.all()

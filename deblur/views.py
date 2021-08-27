from rest_framework import generics

from deblur.models import DeblurData
from deblur.serializers import DeblurDataSerializer


class DeblurDataList(generics.ListCreateAPIView):
    """
    List all illustration sets, or create a new illustration set.
    """

    queryset = DeblurData.objects.all()
    serializer_class = DeblurDataSerializer


class DeblurDataDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete illustration set
    """

    queryset = DeblurData.objects.all()
    serializer_class = DeblurDataSerializer

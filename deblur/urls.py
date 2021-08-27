from django.urls import path, include

from deblur.views import DeblurDataList, DeblurDataDetail

app_name = "deblur"

deblur_patterns = [
    path("deblur/", DeblurDataList.as_view(), name="deblur_list",),
    path("deblur/<int:pk>/", DeblurDataDetail.as_view(), name="deblur_detail",),
]


urlpatterns = [
    path("", include(deblur_patterns)),
]

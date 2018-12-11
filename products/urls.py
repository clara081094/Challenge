from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^productos/$',views.ProductDetailList.as_view())
]

urlpatterns=format_suffix_patterns(urlpatterns)
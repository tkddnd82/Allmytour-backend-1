from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from makers.views import MakerView

urlpatterns = [
    path('', MakerView.as_view()),
    path('/<int:maker_id>',MakerView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

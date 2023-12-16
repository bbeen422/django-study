from django.contrib import admin
from django.urls import path, include
import edu.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('edu/', include('edu.urls')),      # edu app 의 url 을 include 한다.
    path('', edu.views.Index.as_view()),    # 첫 페이지의 url 에 app 이름이 들어가지 않도록 수정한다.
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
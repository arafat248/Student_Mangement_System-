from rest_framework.routers import DefaultRouter
from students.views import students_view


router = DefaultRouter()
router.register('roll', students_view, basename='studentView')

urlpatterns = router.urls

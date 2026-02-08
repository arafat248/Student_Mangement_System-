from rest_framework.routers import DefaultRouter
from students.views import studentview
from subjects.views import subjectview
from results.views import result_view
from report.views import ReportViewSet

router = DefaultRouter()

router.register('student', studentview, basename= 'stud')
router.register('subject', subjectview, basename= 'sub')
router.register('result', result_view, basename= 'res')
router.register('report', ReportViewSet, basename='reports')

urlpatterns = router.urls
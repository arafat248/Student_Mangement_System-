from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from students.models import Student
from results.models import Result
from report.models import Report
from .serializer import report_serial
from django.shortcuts import get_object_or_404

def grade(avg):
    if avg >= 80: return "A+"
    if avg >= 70: return "A"
    if avg >= 60: return "A-"
    if avg >= 50: return "B"
    if avg >= 40: return "C"
    if avg >= 33: return "D"
    return "F"


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = report_serial

    @action(detail=False, methods=['get'], url_path='by-roll/(?P<roll>[^/.]+)')
    def by_roll(self, request, roll=None):
        student = get_object_or_404(student, roll=roll)
        results = Result.objects.filter(student=student).select_related('subject')

        if not results.exists():
            avg = 0
            subjects_list = []
        else:
            avg = sum(r.marks for r in results) / results.count()
            subjects_list = [
                {"subject": r.subject.name, "marks": r.marks}
                for r in results
            ]

        data = {
            "name": student.name,
            "roll": student.roll,
            "class_name": student.class_name,
            "average_marks": avg,
            "grade": grade(avg),
            "subjects": subjects_list
        }

        serializer = report_serial(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
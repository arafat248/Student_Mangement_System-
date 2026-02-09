from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from students.models import Student
from results.models import Result
from report.serializer import report_serial

def calculate_grade(avg):
    if avg >= 80: return "A+"
    if avg >= 70: return "A"
    if avg >= 60: return "A-"
    if avg >= 50: return "B"
    if avg >= 40: return "C"
    if avg >= 33: return "D"
    return "F"

class reportview(ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'], url_path='roll/(?P<roll>[^/.]+)')
    def by_roll(self, request, roll=None):
        student = get_object_or_404(Student, roll=roll)
        results = Result.objects.filter(student=student).select_related('subject')

        if results.exists():
            avg = sum(r.result for r in results) / results.count()
            subjects = [
                {"subject": r.subject.name, "marks": r.result}
                for r in results
            ]
        else:
            avg = 0
            subjects = []
        data = {
            "name": student.name,
            "roll": student.roll,
            "Intake": student.intake,
            "section": student.section,
            "average_marks": round(avg, 2),
            "grade": calculate_grade(avg),
            "subjects": subjects
        }
        return Response(data)

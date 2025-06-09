from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

class ViewPatientRecord(APIView):
    def get(self, request, patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)

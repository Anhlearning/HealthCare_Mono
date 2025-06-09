from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer
from patient.models import Patient
from doctor.models import Doctor

class MakeAppointment(APIView):
    def post(self, request):
        data = request.data
        try:
            patient = Patient.objects.get(id=data['patient_id'])
            doctor = Doctor.objects.get(id=data['doctor_id'])
        except (Patient.DoesNotExist, Doctor.DoesNotExist):
            return Response({"error": "Invalid patient or doctor"}, status=400)

        appointment = Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=data['date']
        )
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=201)

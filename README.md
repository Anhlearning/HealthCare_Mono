# HealthCare_Mono

-- Khởi tạo database và tạo dữ liệu mẫu 
python manage.py migrate
-- THêm dữ liệu mẫu : 
python manage.py shell
# Tạo bệnh nhân
from patient.models import Patient

Patient.objects.create(name="Nguyễn Văn A", age=30, medical_history="Tiểu đường")

Patient.objects.create(name="Trần Thị B", age=45, medical_history="Huyết áp cao")

# Tạo bác sĩ

from doctor.models import Doctor

Doctor.objects.create(name="Bác sĩ Lê Văn C", specialty="Nội khoa")

Doctor.objects.create(name="Bác sĩ Mai Thị D", specialty="Tim mạch")


exit()

API Mẫu
📍 Xem hồ sơ bệnh nhân
http
Copy
Edit
GET http://127.0.0.1:8000/patient/1/
📍 Đặt lịch hẹn
http
Copy
Edit
POST http://127.0.0.1:8000/appointment/make/

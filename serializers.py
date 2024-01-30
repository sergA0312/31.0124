from rest_framework import serializers
from models.models import Doctor, Education, News, Contact, PhoneNumber, Email

class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'

class PhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'doctor', 'address', 'work_time', 'phone_numbers', 'emails']

class DoctorSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    news = NewsSerializer(many=True, read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'image', 'job', 'phone_number', 'description', 'character', 'educations', 'news', 'contacts']
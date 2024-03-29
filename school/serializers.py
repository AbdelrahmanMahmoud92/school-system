from rest_framework import serializers
from .models import Student, FirstClassRoom, SecondClassRoom, LastClassRoom

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        extra_kwargs = {
            'approval_status' : {'read_only' : True},
        }


class FirstClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        ref_name = 'FirstClassSchool'


class SecondClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        ref_name = 'SecondClassSchool'


class LastClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        ref_name = 'LastClassSchool'

# _________________________________________________________________________________________________________#

class FirstClassRoomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.filter(school_year='First_class'), many=True)

    class Meta:
        model = FirstClassRoom
        fields = ['room', 'students']
        ref_name = 'FirstClassRoomSchool'

    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(first_class_rooms__room=room_name, first_class_rooms__approval_status=FirstClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]


class SecondClassRoomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.filter(school_year='Second_class'), many=True)
    
    class Meta:
        model = SecondClassRoom
        fields = [ 'room', 'students']
        ref_name = 'SecondClassRoomSchool'

    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(second_class_rooms__room=room_name, second_class_rooms__approval_status=SecondClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]


class LastClassRoomSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.filter(school_year='Last_class'), many=True)
    class Meta:
        model = LastClassRoom
        fields = [ 'room', 'students']
        ref_name = 'LastClassRoomSchool'

    def get_students_by_room(self, room_name):
        students_in_room = Student.objects.filter(last_class_rooms__room=room_name, last_class_rooms__approval_status=LastClassRoom.Status.APPROVED)
        return [student.name for student in students_in_room]
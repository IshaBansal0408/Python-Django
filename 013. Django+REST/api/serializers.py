from rest_framework import serializers

class StudentSerial(serializers.Serializer):
    name = serializers.CharField()
    rollNo = serializers.IntegerField()
    marks = serializers.IntegerField()
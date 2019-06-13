from rest_framework import serializers
from .models import books



class booksserializer(serializers.Serializer):
	bname=serializers.CharField(max_length=100)
	bauthor=serializers.CharField(max_length=200)
	bquan=serializers.CharField(max_length=500)



class booksModelSerializer(serializers.ModelSerializer):
	class Meta:
		

		model=books
		fields='__all__'

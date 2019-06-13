from django.shortcuts import render


from .models import books
from .serializer import booksserializer,booksModelSerializer
from rest_framework.viewsets import ModelViewSet



class bookViewSet(ModelViewSet):

	model=books
	serializer_class=booksModelSerializer
	permission_class=()
	queryset=books.objects.all()


def get_query(self):

	if 'bquan' in self.request.GET:

		return books.objects.filter(bquan=self.reuest.GET['bquan'])

	else:

		return books.objects.all()




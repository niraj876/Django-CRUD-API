from rest_framework.response import Response
from .models import EmployeeModel
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.views import APIView


class EmployeeViewAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            emp = EmployeeModel.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data)

        emp = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = EmployeeModel.objects.get(pk=id)
        serializer = EmployeeSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = EmployeeModel.objects.get(pk=id)
        serializer = EmployeeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = EmployeeModel.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})
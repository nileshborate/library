from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterUserAPI(APIView):
    def post(self,request):
        serializers = UserSerializer(data =request.data)
        if not serializers.is_valid():
            print(serializers.error)
            return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
        serializers.save()

        user = User.objects.get(username=serializers.data["username"])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializers.data,'token':str(token_obj),'message':'User added Successfully'})

class MemberAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        if request.GET.get('id'):
            members_objs = Member.objects.get(id=request.GET.get('id'))
            serializers = MemberSerializer(members_objs)
        else:
            members_objs = Member.objects.all()
            serializers = MemberSerializer(members_objs,many=True)
        return Response({'status':200,'payload':serializers.data})


    def post(self,request):
        serializers = MemberSerializer(data = request.data)
        if not serializers.is_valid():
            print(serializers.error)
            return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
        serializers.save()
        return Response({'status':200,'payload':serializers.data,'message':'Member added Successfully'})

    def put(self,request):
        try:
            member_obj = Member.objects.get(id=request.data['id'])
            serializers = MemberSerializer(member_obj,data = request.data)
            if not serializers.is_valid():
                print(serializers.error)
                return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
            serializers.save()
            return Response({'status':200,'payload':serializers.data,'message':'Member updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is Wrong'})

    def delete(self,request):
        try:
            id=request.GET.get('id')
            members_objs = Member.objects.get(id=id)
            members_objs.delete()
            return Response({'status':200,'payload':'Member Deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is Wrong'})



class BookAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        if request.GET.get('id'):
            books_objs = Book.objects.get(id=request.GET.get('id'))
            serializers = BookSerializer(books_objs)
        else:
            books_objs = Book.objects.all()
            serializers = BookSerializer(books_objs,many=True)
        return Response({'status':200,'payload':serializers.data})
     
    def post(self,request):
        serializers = BookSerializer(data = request.data)
        if not serializers.is_valid():
            print(serializers.error)
            return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
        serializers.save()
        return Response({'status':200,'payload':serializers.data,'message':'Book added Successfully'})
     
    def put(self,request):
        try:
            book_obj = Book.objects.get(id=request.data['id'])
            serializers = BookSerializer(book_obj,data = request.data)
            if not serializers.is_valid():
                print(serializers.error)
                return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
            serializers.save()
            return Response({'status':200,'payload':serializers.data,'message':'Book updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is Wrong'})
    
    def patch(self,request):
        try:
            book_obj = Book.objects.get(id=request.data['id'])
            serializers = BookSerializer(book_obj,data = request.data,partial=True)
            if not serializers.is_valid():
                print(serializers.error)
                return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
            serializers.save()
            return Response({'status':200,'payload':serializers.data,'message':'Book updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is Wrong'})
    
    def delete(self,request):
        try:
            id=request.GET.get('id')
            book_obj = Book.objects.get(id=id)
            book_obj.delete()
            return Response({'status':200,'payload':'Book Deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is Wrong'})
     

class LoanAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        if request.GET.get('id'):
            loan_obj = Loan.objects.get(id=request.GET.get('id'))
            serializers = LoanSerializer(loan_obj)
        else:
            loan_obj = Loan.objects.all()
            serializers = LoanSerializer(loan_obj,many=True)
        return Response({'status':200,'payload':serializers.data})

    def post(self,request):
        try:
            serializers = LoanSerializer(data=request.data)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
            serializers.save()
            return Response({'status':200,'payload':serializers.data,'message':'Loan Added Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is wrong'})

    def put(self,request):
        try:
            loan_obj = Loan.objects.get(id=request.data["id"])
            serializers = LoanSerializer(loan_obj,data=request.data)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
            serializers.save()
            return Response({'status':200,'payload':serializers.data,'message':'Loan Updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is wrong'})
    
    def patch(self,request):
        try:
            loan_obj = Loan.objects.get(id=request.data["id"])
            serializers = LoanSerializer(loan_obj,data=request.data,partial=True)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status':403,'errors':serializers.errors,'message':'Invalid Input'})
            serializers.save()
            return Response({'status':200,'payload':serializers.data,'message':'Loan Updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Something is wrong'})
    
    def delete(self,request):
        try:
            loan_obj = Loan.objects.get(id=request.data["id"])
            loan_obj.delete()
            return Response({"status":200,"message":"Loan Deleted"})
        except Exception as e:
            print(e)
            return Response({"status":403,"message":"Something is Wrong"})


class ReturnBookAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        if request.GET.get('id'):
            returnbook = ReturnBook.objects.get(id=request.GET.get('id'))
            serializers = ReturnBookSerializer(returnbook)
        else:
            returnbook = ReturnBook.objects.all()
            serializers = ReturnBookSerializer(returnbook,many=True)
        return Response({'status':200,'payload':serializers.data})

    def post(self,request):
        try:
            serializers = ReturnBookSerializer(data=request.data)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({"status":403,"errors":serializers.errors,"message":"Invalid Input"})
            serializers.save()
            return Response({"status":200,"payload":serializers.data,"message":"Return Book Added Successfully"})
        except Exception as e:
            print(e)
            return Response({"status":403,"message":"Something is wrong"})
    
    def put(self,request):
        try:
            returnbook = ReturnBook.objects.get(id = request.data["id"])
            serializers = ReturnBookSerializer(returnbook,data=request.data)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({"status":403,"errors":serializers.errors,"message":"Invalid Input"})
            serializers.save()
            return Response({"status":200,"payload":serializers.data,"message":"Return Book Updated Successfully"})
        except Exception as e:
            print(e)
            return Response({"status":403,"message":"Something is wrong"})
    
    def patch(self,request):
        try:
            returnbook = ReturnBook.objects.get(id = request.data["id"])
            serializers = ReturnBookSerializer(returnbook,data=request.data,partial=True)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({"status":403,"errors":serializers.errors,"message":"Invalid Input"})
            serializers.save()
            return Response({"status":200,"payload":serializers.data,"message":"Return Book Updated Successfully"})
        except Exception as e:
            print(e)
            return Response({"status":403,"message":"Something is wrong"})
    
    def delete(self,request):
        try:
            returnbook = ReturnBook.objects.get(id = request.data["id"])
            returnbook.delete()
            return Response({"status":200,"message":"Return Book Deleted Successfully"})
        except Exception as e:
            print(e)
            return Response({"status":403,"message":"Something is wrong"})   


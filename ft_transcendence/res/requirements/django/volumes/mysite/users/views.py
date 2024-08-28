from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound

from django.http import JsonResponse
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.

# users/list
class UsersAPIView(APIView):
	# GET : 유저 목록 조회
	def get(self, request):
		users = CustomUser.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	# POST : 유저 등록
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# DELETE: 유저 삭제
	def delete(self, request, id):
		user = get_object_or_404(CustomUser, id=id)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# users/list/(id)
class UserAPIView(APIView):
	# GET : 유저 조회
	def get(self, request, id):
		user = get_object_or_404(CustomUser, id=id)
		serializer = UserSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	# PUT : 유저 정보 수정
	def put(self, request, id):
		user = get_object_or_404(CustomUser, id=id)
		serializer = UserSerializer(user, data=request.data, partial=True)  # partial=True로 부분 업데이트 가능
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	# POST: 친구 추가
	def post(self, request, id):
		user = get_object_or_404(CustomUser, id=id)
		friend_username = request.data.get('friend_username')
		if not friend_username:
			return Response({"error": "No friend_username provided"}, status=status.HTTP_400_BAD_REQUEST)
	    # 친구를 username으로 찾기
		try:
			friend = CustomUser.objects.get(username=friend_username)
		except CustomUser.DoesNotExist:
			raise NotFound(detail="Friend with the given username does not exist.")
		user.friends.add(friend)
		user.save()
		return Response({"status": "Friend added"}, status=status.HTTP_200_OK)
	
	# DELETE: 친구 삭제
	def delete(self, request, id):
		user = get_object_or_404(CustomUser, id=id)
		friend_username = request.data.get('friend_username')
		if not friend_username:
			return Response({"error": "No friend_username provided"}, status=status.HTTP_400_BAD_REQUEST)
		# 친구를 username으로 찾기
		try:
			friend = CustomUser.objects.get(username=friend_username)
		except CustomUser.DoesNotExist:
			raise NotFound(detail="Friend with the given username does not exist.")
		if friend not in user.friends.all():
			return Response({"error": "Friend is not in the user's friend list"}, status=status.HTTP_400_BAD_REQUEST)
		user.friends.remove(friend)
		user.save()
		return Response({"status": "Friend removed"}, status=status.HTTP_200_OK)

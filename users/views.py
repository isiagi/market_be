from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


class AuthViewSet(viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        return CustomUserSerializer

    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if not user:
            return Response(
                {'error': 'Invalid credentials'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'seller_type': user.seller_type
        })

    @action(detail=False, methods=['post'])
    @permission_classes([AllowAny])
    def signup(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Check if user exists
        if CustomUser.objects.filter(email=serializer.validated_data['email']).exists():
            return Response(
                {'error': 'User with this email already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # If is_employer is True, is_applicant should be False, create employer profile
        # if serializer.validated_data['is_employer']:
        #     # serializer.validated_data['is_applicant'] = False
        #     # create employer profile
        #     EmployerProfile.objects.create(user=serializer.save())


        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'seller_type': user.seller_type
        }, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put', 'patch'])
    @permission_classes([AllowAny])
    def update_profile(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_user = serializer.save()
        
        return Response({
            'user_id': updated_user.id,
            'username': updated_user.username,
            'email': updated_user.email
        })
    
   #In your ViewSet class:
    permission_classes([IsAuthenticated])
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Logged out successfully'})
        except AttributeError:
            return Response({'error': 'User not authenticated'}, status=401)
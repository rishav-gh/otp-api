from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_tophone
from .models import User
from django.utils.crypto import get_random_string

@api_view(['POST'])
def send_otp(request):
    data = request.data
    phone_no = data.get('phone_no')
    password = data.get('password')

    if not phone_no:
        return Response({
            'status': 400,
            'message': 'Phone number is required'
        })
    
    if not password:
        return Response({
            'status': 400,
            'message': 'Password is required'
        })

    # Check if user with the same phone number already exists
    if User.objects.filter(phone_no=phone_no).exists():
        return Response({
            'status': 400,
            'message': 'User with this phone number already exists'
        })

    # Generate a unique username
    username = get_random_string(10)

    # Ensure the generated username is unique
    while User.objects.filter(username=username).exists():
        username = get_random_string(10)

    # Create a new user with a unique username
    user = User.objects.create(
        phone_no=phone_no,
        username=username,
        otp=send_otp_tophone(phone_no)
    )
    user.set_password(password)
    user.save()

    return Response({
        'status': 200,
        'message': 'OTP sent'
    })

@api_view(['POST'])
def verify_otp(request):
    data = request.data
    phone_no = data.get('phone_no')
    otp = data.get('otp')

    if not phone_no:
        return Response({
            'status': 400,
            'message': 'Phone number is required'
        })
    
    if not otp:
        return Response({
            'status': 400,
            'message': 'OTP is required'
        })

    try:
        user = User.objects.get(phone_no=phone_no, otp=otp)
        # If OTP matches, you can mark the user as verified or perform any other action
        user.is_verified=True  
        user.save()
        return Response({
            'status': 200,
            'message': 'OTP verified successfully'
        })
    except User.DoesNotExist:
        return Response({
            'status': 400,
            'message': 'Invalid phone number or OTP'
        })
from rest_framework.response import Response

from .models import MyUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

from .serializers import UserProfileSerializer


class UserProfileAPIView(APIView):
    def get(self, request):
        """
        Returns the profile information of the user making the request.

        GET /profile

        Returns:
            Response: The user's profile information.
        """
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


from .serializers import RegisterSerializer


class RegisterAPIVIew(APIView):
    permission_classes = []

    def post(self, request):
        """
        Creates a new user. Will return HTTP 201 Created if successful.
        The request body should contain the following:
        - username (string): The username for the new user.
        - password (string): The password for the new user.
        - confirm_password (string): The password for the new user again for confirmation.
        - email (string): The email for the new user.
        - first_name (string): The first name for the new user.
        - last_name (string): The last name for the new user.
        """

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request):
        """
        Blacklists the refresh token and logs out the user.
        The request body should contain the following:
        - refresh (string): The refresh token to be blacklisted.
        """
        try:
            print(request.data.get("refresh"))
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


from .serializers import ChangePasswordSerializer


class ChangePasswordAPIView(APIView):
    def post(self, request):
        """
        Changes the password of the user making the request.
        The request body should contain the following:
        - old_password (string): The old password of the user.
        - new_password (string): The new password for the user.
        - confirm_password (string): The new password for the user again for confirmation.
        """
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]

            if not user.check_password(old_password):
                return Response(
                    {"error": "Old password is incorrect"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(new_password)
            user.save()

            RefreshToken.for_user(user)

            return Response(
                {"message": "Password changed successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileAPIView(APIView):
    def patch(self, request):
        """
        Partially updates the user's profile information with the provided data.

        The request should contain fields to update such as 'username', 'email',
        'first_name', or 'last_name'. Only the fields provided will be updated.

        Returns:
            Response: The updated user profile information if successful, or
            validation errors if the input data is invalid.
        """

        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

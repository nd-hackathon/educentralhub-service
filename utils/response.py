from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import uuid

def generate_meta(status_code):
    return {
        "status_code": status_code,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "request_id": str(uuid.uuid4()),
    }

def success_response(data=None, message="Request successful", status_code=status.HTTP_200_OK):
    return Response({
        "success": True,
        "message": message,
        "data": data if isinstance(data, dict) else {"data": data},
        "error": None,
        "meta": generate_meta(status_code)
    }, status=status_code)

def error_response(message="An error occurred", error_details=None, status_code=status.HTTP_400_BAD_REQUEST):
    return Response({
        "success": False,
        "message": message,
        "data": None,
        "error": error_details if error_details else {"detail": message},
        "meta": generate_meta(status_code)
    }, status=status_code)

def HTTP_200(data):
    return success_response(data, "OK", status.HTTP_200_OK)

def HTTP_201(data):
    return success_response(data, "Created successfully", status.HTTP_201_CREATED)

def HTTP_202(data):
    return success_response(data, "Accepted", status.HTTP_202_ACCEPTED)

def HTTP_204():
    return success_response(None, "No Content", status.HTTP_204_NO_CONTENT)

def HTTP_400(message="Bad Request", error_details=None):
    return error_response(message, error_details, status.HTTP_400_BAD_REQUEST)

def HTTP_401(message="Unauthorized access", error_details=None):
    return error_response(message, error_details, status.HTTP_401_UNAUTHORIZED)

def HTTP_403(message="Forbidden", error_details=None):
    return error_response(message, error_details, status.HTTP_403_FORBIDDEN)

def HTTP_404(message="Resource not found", error_details=None):
    return error_response(message, error_details, status.HTTP_404_NOT_FOUND)

def HTTP_307(data):
    return success_response(data, "Temporary Redirect", status.HTTP_307_TEMPORARY_REDIRECT)

def HTTP_408(message="Request Timeout", error_details=None):
    return error_response(message, error_details, status.HTTP_408_REQUEST_TIMEOUT)

def HTTP_500(message="Internal Server Error", error_details=None):
    return error_response(message, error_details, status.HTTP_500_INTERNAL_SERVER_ERROR)

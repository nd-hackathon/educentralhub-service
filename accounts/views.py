from utils.response import *
from rest_framework.views import APIView

class TestAPI(APIView):
    """_summary_

    Args:
        APIView (_type_): _description_
    """
    def get(self, request,*args,**kwargs):
        data = "Testing API successfully fetched."
        return HTTP_200(data=data)

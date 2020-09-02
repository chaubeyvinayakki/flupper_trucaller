from django.conf import settings
from rest_framework.response import Response


class SuccessResponse(Response):
    """
        Custom success response class
    """
    def __init__(self, data=None, status=None):
        result = {"status": None, "data": None, "error":None}
        result.update({
                        "status": 200,
                        "data": data,
                        "error": None
                     })
        return super().__init__(data=result, status=status)

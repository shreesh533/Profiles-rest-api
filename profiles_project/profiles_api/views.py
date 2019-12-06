from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class HelloApiView(APIView):
    """Test API View"""

    # def get(self, request, format=None):
    #     """retrn a list of APIView features"""
    #     an_apiview = [1, 2, 3, 4]
    #     print("Came here")
    #     return Response({"Messsage": "Hello", "an_apiview": an_apiview})

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_api_view = [1, 2, 3, 4]
        print("Came here")
        return Response({"Message": "Hello", "an_api_view": an_api_view})


@api_view(["GET", "POST"])
def hello_world(request):
    print("Came ere 0")
    an_api_view = [1, 2, 3, 4]
    print("Came here")
    return Response({"Messsage": "Hello", "an_apiview": an_api_view})
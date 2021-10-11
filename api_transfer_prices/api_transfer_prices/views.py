from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, json

@api_view(['POST'])
def TransferViewSet(request, name_srv, username, password):
    if request.method == 'POST':
        session = requests.Session()
        address = f"https://{name_srv}/index.php?route=api/login"        
        answer = json.loads(session.post(
            address,
            data={'username':username, 'password':password}
        ).text)
        cookie = answer['cookie']
        address_prod = f'https://{name_srv}/index.php?route=api/custom/products/'
        return Response(json.loads(session.get(address_prod, params={'api_token':cookie}).text))
 
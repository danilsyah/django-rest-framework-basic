import json
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import  Response

from products.models import Product


# Create your views here.
# def api_home(request, *args,**kwargs):
    # request -> httpRequest -> Django
    # print(request.GET)
    # print(request.POST)
    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # # return JsonResponse({"message":"Hi there, this is your Django API response!!!"})
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # return JsonResponse(data)

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data['id'] = model_data.id
#         data['title']= model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price
#     return JsonResponse(data)

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # if request.method != "POST":
    #     return Response({"detail":"GET Not Allowed"}, status=405)
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price'])
    return Response(data)
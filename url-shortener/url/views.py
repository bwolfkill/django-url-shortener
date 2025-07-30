from django.shortcuts import redirect, render
from url.models import URL
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from rest_framework.decorators import api_view
import hashlib
from url.serializers import URLSerializer
from rest_framework.response import Response

# Create your views here.
def redirect_original_url(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        url.visits += 1
        url.save()
        return redirect(url.url)
    except URL.DoesNotExist:
        return HttpResponseNotFound("Short URL not found")
    

@api_view(['POST'])
def create_short_url(request):
    if 'url' in request.data:
        original_url = request.data['url']

        if URL.objects.filter(url=original_url).exists():
            existing_url = URL.objects.get(url=original_url)
            return JsonResponse({'short_url': f'localhost:8000/url/{existing_url.hash}'}, status=200)

        hash_value = hashlib.md5(original_url.encode()).hexdigest()[:10]

        url = URL.objects.create(hash=hash_value, url=original_url)

        return JsonResponse({'short_url': f'localhost:8000/url/{hash_value}'}, status=201)
    
    return JsonResponse({'error': 'Invalid request data'}, status=400)


@api_view(['GET'])
def get_url_details(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        serializer = URLSerializer(url)
        return Response(serializer.data)
    except URL.DoesNotExist:
        return Response({'error': "Short URL not found"}, status=404)


def simple_ui(request):
    urls = URL.objects.all()
    return render(request, "index.html", {'urls': urls})

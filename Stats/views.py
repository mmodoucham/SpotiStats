from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer PutAuthTokenHere',
}


# Create your views here.
def IndexView(request):
    params = (
        ('time_range', 'medium_term'),
        ('limit', '50'),
        ('offset', '0'),
    )

    response = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers, params=params)
    data = response.json()
    return JsonResponse(data['items'], safe=False)


def ArtistShort(request):
    params = (
        ('time_range', 'short_term'),
        ('limit', '50'),
        ('offset', '0'),
    )

    response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers, params=params)
    data = response.json()
    data = data['items']
    names = []
    images = []
    url = []
    counter = []

    for i in range(0, 50, 1):
        counter.append(i)
        names.append(data[i])
    context = {
        'artist_name': names,
    }

    return render(request, 'index.html', context)


def ArtistMedium(request):
    params = (
        ('time_range', 'medium_term'),
        ('limit', '50'),
        ('offset', '0'),
    )

    response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers, params=params)
    data = response.json()
    data = data['items']
    names = []
    images = []
    url = []
    counter = []

    for i in range(0, 50, 1):
        counter.append(i)
        names.append(data[i])

    context = {
        'artist_name': names,
    }

    return render(request, 'index.html', context)


def ArtistLong(request):
    params = (
        ('time_range', 'long_term'),
        ('limit', '50'),
        ('offset', '0'),
    )

    response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers, params=params)
    data = response.json()
    data = data['items']
    names = []
    images = []
    url = []
    counter = []

    for i in range(0, 50, 1):
        counter.append(i)
        names.append(data[i])
    context = {
        'artist_name': names,
    }

    return render(request, 'index.html', context)


def TrackShort(request):
    params = (
        ('time_range', 'short_term'),
        ('limit', '50'),
        ('offset', '0'),
    )

    response = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers, params=params)
    data = response.json()
    data = data['items']
    names = []
    images = []
    url = []
    counter = []

    for i in range(0, 50, 1):
        counter.append(i)
        names.append(data[i])

    print(data[1]['album']['artists'][0]['name'])
    context = {
        'artist_name': names,
    }

    return render(request, 'tracks.html', context)


def TrackMedium(request):
    params = (
        ('time_range', 'medium_term'),
        ('limit', '50'),
        ('offset', '0'),
    )

    response = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers, params=params)
    data = response.json()
    data = data['items']
    names = []
    images = []
    url = []
    counter = []

    for i in range(0, 50, 1):
        counter.append(i)
        names.append(data[i])

    print(data[1]['album']['artists'][0]['name'])
    context = {
        'artist_name': names,
    }

    return render(request, 'tracks.html', context)


def TrackLong(request):
    params = (
        ('time_range', 'long_term'),
        ('limit', '50'),
        ('offset', '0'),
    )

    response = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers, params=params)
    data = response.json()
    data = data['items']
    names = []
    images = []
    url = []
    counter = []

    for i in range(0, 50, 1):
        counter.append(i)
        names.append(data[i])

    print(data[1]['album']['artists'][0]['name'])
    context = {
        'artist_name': names,
    }

    return render(request, 'tracks.html', context)

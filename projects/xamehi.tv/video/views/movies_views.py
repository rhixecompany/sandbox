<<<<<<< HEAD
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status

from video.models import Movies
from video.serializers import MoviesSerializer


@api_view(['GET'])
def getMovies(request):
    query = request.query_params.get('keyword')

    if query == None:
        query = ''

    movies = Movies.objects.filter(
        name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(movies, 5)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = MoviesSerializer(movies, many=True)
    return Response({'movies': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def getTopMovies(request):
    movies = Movies.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = MoviesSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMovie(request, pk):
    movie = Movies.objects.get(_id=pk)
    serializer = MoviesSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createMovie(request):
    user = request.user

    movie = Movies.objects.create(
        user=user,
        name="Sample Name",
        file="/media/movies/Mortal_Kombat_Legends_Snow_Blind_2022_NetNaija.com.mp4",
        image="/media/images/MortalKombatLegends.png",
        rating=1.00,
        numReviews=1,
        description='',
    )

    serializer = MoviesSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateMovie(request, pk):
    data = request.data
    movie = Movies.objects.get(_id=pk)

    movie.name = data['name']
    movie.file = data['file']
    movie.image = data['image']
    movie.rating = data['rating']
    movie.numReviews = data['numReviews']
    movie.description = data['description']

    movie.save()

    serializer = MoviesSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteMovie(request, pk):
    movie = Movies.objects.get(_id=pk)
    movie.delete()
    return Response('Movie Deleted')


@api_view(['POST'])
def uploadFile(request):
    data = request.data

    movie_id = data['movie_id']
    movie = Movies.objects.get(_id=movie_id)

    movie.file = request.FILES.get('file')
    movie.save()

    return Response('Video was uploaded')
=======
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status

from video.models import Movies
from video.serializers import MoviesSerializer


@api_view(['GET'])
def getMovies(request):
    query = request.query_params.get('keyword')

    if query == None:
        query = ''

    movies = Movies.objects.filter(
        name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(movies, 5)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = MoviesSerializer(movies, many=True)
    return Response({'movies': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def getTopMovies(request):
    movies = Movies.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = MoviesSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMovie(request, pk):
    movie = Movies.objects.get(_id=pk)
    serializer = MoviesSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createMovie(request):
    user = request.user

    movie = Movies.objects.create(
        user=user,
        name="Sample Name",
        file="/media/movies/Mortal_Kombat_Legends_Snow_Blind_2022_NetNaija.com.mp4",
        image="/media/images/MortalKombatLegends.png",
        rating=1.00,
        numReviews=1,
        description='',
    )

    serializer = MoviesSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateMovie(request, pk):
    data = request.data
    movie = Movies.objects.get(_id=pk)

    movie.name = data['name']
    movie.file = data['file']
    movie.image = data['image']
    movie.rating = data['rating']
    movie.numReviews = data['numReviews']
    movie.description = data['description']

    movie.save()

    serializer = MoviesSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteMovie(request, pk):
    movie = Movies.objects.get(_id=pk)
    movie.delete()
    return Response('Movie Deleted')


@api_view(['POST'])
def uploadFile(request):
    data = request.data

    movie_id = data['movie_id']
    movie = Movies.objects.get(_id=movie_id)

    movie.file = request.FILES.get('file')
    movie.save()

    return Response('Video was uploaded')
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)

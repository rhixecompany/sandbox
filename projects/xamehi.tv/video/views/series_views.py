from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status

from video.models import Series
from video.serializers import SeriesSerializer


@api_view(['GET'])
def getSeries(request):
    query = request.query_params.get('keyword')

    if query == None:
        query = ''

    series = Series.objects.filter(
        name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(series, 5)

    try:
        series = paginator.page(page)
    except PageNotAnInteger:
        series = paginator.page(1)
    except EmptyPage:
        series = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = SeriesSerializer(series, many=True)
    return Response({'series': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def getTopSeries(request):
    series = Series.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = SeriesSerializer(series, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSerie(request, pk):
    serie = Series.objects.get(_id=pk)
    serializer = SeriesSerializer(serie, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createSeries(request):
    user = request.user

    series = Series.objects.create(
        user=user,
        name="Sample Name",
        file="/media/episodes/Mortal_Kombat_Legends_Snow_Blind_2022_NetNaija.com.mp4",
        image="/media/images/MortalKombatLegends.png",
        rating=1.00,
        numReviews=1,
        description='',
    )

    serializer = SeriesSerializer(series, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateSeries(request, pk):
    data = request.data
    series = Series.objects.get(_id=pk)

    series.name = data['name']
    series.file = data['file']
    series.image = data['image']
    series.rating = data['rating']
    series.numReviews = data['numReviews']
    series.description = data['description']

    series.save()

    serializer = SeriesSerializer(series, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteSeries(request, pk):
    series = Series.objects.get(_id=pk)
    series.delete()
    return Response('Series Deleted')


@api_view(['POST'])
def uploadImage(request):
    data = request.data

    series_id = data['series_id']
    series = Series.objects.get(_id=series_id)

    series.image = request.FILES.get('image')
    series.save()

    return Response('Image was uploaded')

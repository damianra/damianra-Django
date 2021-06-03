from django.shortcuts import render
from btcdata.models import BtcData
from btcdata.rest_serializer import BtcSerializer
from rest_framework import routers, viewsets, request, generics
from django.core.paginator import Paginator
from blog.models import Menu, RedesSociales, Proyecto


# Create your views here.
def btcdata(request):
    btc_data = BtcData.objects.order_by('date')
    menu = Menu.objects.order_by('id')
    proyectos =  Proyecto.objects.all().order_by('-fecha').filter(estado='Publicado')[:5]
    redes = RedesSociales.objects.all()


    contenido = {'btcdata': btc_data, 'Github': redes[0].link, 'Linkedin': redes[1].link, 'proyectos': proyectos, 'menu': menu}
    return render(request, 'btcdata/btc_table.html', contenido)


class BtcViewSet(generics.ListAPIView):
    serializer_class = BtcSerializer

    def get_queryset(self):
        queryset = BtcData.objects.all()
        date = self.request.query_params.get('date', None)
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)

        if start and end is not None:
            queryset = queryset.filter(date__gte=start, date__lte=end)
        else:
            if start is not None:
                queryset = queryset.filter(date__gte=start)
            if end is not None:
                queryset = queryset.filter(date__lte=end)
        if date is not None:
            queryset = queryset.filter(date=date)

        return queryset
    


    



    




from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    filename = 'data.xlsx'

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, XLSXRenderer]

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            return Post.objects.filter(thedate__range=[start_date, end_date])
        elif start_date:
            return Post.objects.filter(thedate__range=[start_date, '9999-12-31'])
        elif end_date:
            return Post.objects.filter(thedate__range=['0001-01-01', end_date])

        return Post.objects.all()

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(
            request, response, *args, **kwargs
        )
        if (
                isinstance(response, Response)
                and response.accepted_renderer.format == "xlsx"
        ):
            response["content-disposition"] = "attachment; filename={}".format(
                self.get_filename(),
            )

        return response

    def get_filename(self):
        return self.filename

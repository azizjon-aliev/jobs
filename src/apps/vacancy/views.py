import logging

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Skill
from .serializers import SkillSerializer

logger = logging.getLogger(__name__)


class SkillAPIView(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def list(self, request, *args, **kwargs):
        logger.info(f"Listing skills")
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

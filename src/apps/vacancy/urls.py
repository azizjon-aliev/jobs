from rest_framework import routers
from .views import SkillAPIView

router = routers.DefaultRouter()
router.register(r'', SkillAPIView, basename='vacancies')

urlpatterns = router.urls

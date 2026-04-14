from django.urls import path

from .views import feature_page, home

urlpatterns = [
    path("", home, name="home"),
    path("explore/", feature_page, {"page_key": "explore"}, name="explore"),
    path("ai-tutor/", feature_page, {"page_key": "ai-tutor"}, name="ai_tutor"),
    path("progress/", feature_page, {"page_key": "progress"}, name="progress"),
    path("more/", feature_page, {"page_key": "more"}, name="more"),
]

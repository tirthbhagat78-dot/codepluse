from django.urls import path

from .views import feature_page, home, lesson_detail, lessons

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", home, name="dashboard"),
    path("lessons/", lessons, name="lessons"),
    path("lessons/<slug:slug>/", lesson_detail, name="lesson_detail"),
    path("explore/", feature_page, {"page_key": "explore"}, name="explore"),
    path("ai-tutor/", feature_page, {"page_key": "ai-tutor"}, name="ai_tutor"),
    path("my-notes/", feature_page, {"page_key": "my-notes"}, name="my_notes"),
    path("cheat-sheets/", feature_page, {"page_key": "cheat-sheets"}, name="cheat_sheets"),
    path("help-center/", feature_page, {"page_key": "help-center"}, name="help_center"),
    path("bookmarks/", feature_page, {"page_key": "bookmarks"}, name="bookmarks"),
    path("study-goals/", feature_page, {"page_key": "study-goals"}, name="study_goals"),
    path("progress/", feature_page, {"page_key": "progress"}, name="progress"),
    path("more/", feature_page, {"page_key": "more"}, name="more"),
]

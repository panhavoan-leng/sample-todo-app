from django.urls import path
from app.todo.views import TodoView

urlpatterns = [
    path("", TodoView.as_view({"get": "list_todo"}), name="list_todo"),
    path("", TodoView.as_view({"post"}), name="create_todo"),
    path("<int:id>/detail", TodoView.as_view({"get": "detail_todo"}), name="detail_todo"),
    path("<int:id>/update", TodoView.as_view({"put": "update_todo"}), name="update_todo"),
    path("<int:id>/delete", TodoView.as_view({"delete": "delete_todo"}), name="delete_todo"),
    path("<int:id>/mark_as_complete", TodoView.as_view({"put": "mark_as_complete"}), name="mark_as_complete"),
]

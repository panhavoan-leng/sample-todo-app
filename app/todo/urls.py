from django.urls import path
from app.todo.views import TodoView

urlpatterns = [
    path("", TodoView.as_view({"get": "list_todo"}), name="list_todo"),
    path("", TodoView.as_view({"post"}), name="create_todo"),
    path(
        "<int:id>/detail",
        TodoView.as_view(
            {
                "get": "detail_todo",
            }
        ),
        name="detail_todo",
    ),
    path("<int:id>/update", TodoView.as_view({"put": "update_todo"}), name="update_todo"),
]

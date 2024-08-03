from django.urls import path
from api.views import *

urlpatterns = [
    path("create_user", UserCreation.as_view({'post':'createuser'})),
    path('add_note', CreateNote.as_view({"get":"get_notes", "post":"create_notes"}))
]
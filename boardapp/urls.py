from django.urls import path
from .views import sign_up_function, login_func, list_function, logout_function, detail_function, good_function, BoardCreate


urlpatterns = [
    path('sign_up/', sign_up_function, name="sign_up"),
    path('login/', login_func, name="login"),
    path('logout/', logout_function, name="logout"),
    path('list/', list_function, name="list"),
    path("detail/<int:pk>", detail_function, name="detail"),
    path("good/<int:pk>", good_function, name="good"),
    path("create/", BoardCreate.as_view(), name="create")
]

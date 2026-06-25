from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .restapis import (
    analyze_review_sentiments,
    get_request,
    post_review,
)

app_name = "djangoapp"

urlpatterns = [
    # Path for registration
    path("registration", views.registration, name="registration"),

    # Path for login/logout
    path("login", views.login_user, name="login"),
    path("logout", views.logout_request, name="logout"),

    # Path for user registration
    path("register", views.registration, name="register"),

    # Path for car data
    path("get_cars", views.get_cars, name="getcars"),

    # Path for dealerships
    path(
        "get_dealers/",
        views.get_dealerships,
        name="get_dealers",
    ),
    path(
        "get_dealers/<str:state>",
        views.get_dealerships,
        name="get_dealers_by_state",
    ),

    # Path for dealer details
    path(
        "dealer/<int:dealer_id>",
        views.get_dealer_details,
        name="dealer_details",
    ),

    # Path for dealer reviews
    path(
        "reviews/dealer/<int:dealer_id>",
        views.get_dealer_reviews,
        name="dealer_reviews",
    ),

    # Path for adding reviews
    path(
        "add_review",
        views.add_review,
        name="add_review",
    ),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

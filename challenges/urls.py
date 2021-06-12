from django.urls import path
from . import views

urlpatterns = [
    # path('january',views.january),
    # path('feburary',views.feburary),
    # path('march',views.march),
    path("",views.index),
    path("<int:month>",views.monthly_challenges_by_number),
    path("<str:month>",views.monthly_challenges, name="monthly_challenges"),
]

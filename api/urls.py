from django.urls import path
from .views import TicketList, CreateTicket, TicketDetail, TicketVerification, MemberList, MemberDetail

urlpatterns =[
    path('tickets/', TicketList.as_view()),
    path('tickets/<int:pk>', TicketDetail.as_view()),
    path('tickets/create', CreateTicket.as_view()),
    path('tickets/verification', TicketVerification.as_view()),
    path('member/', MemberList.as_view()),
    path('member/<int:pk>', MemberDetail.as_view()),
]
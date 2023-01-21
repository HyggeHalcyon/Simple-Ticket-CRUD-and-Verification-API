from rest_framework import generics, status
from rest_framework.response import Response
from .models import TicketOrder, Member
from .serializers import TicketSerializers, CreateTicketSerializers, VerificationSerializers, MemberSerializers

class TicketList(generics.ListAPIView):
    serializer_class = TicketSerializers

    def get_queryset(self):
        queryset = TicketOrder.objects.all()
        Member = self.request.query_params.get('member')
        if Member is not None:
            queryset = queryset.filter(Order=Member)
        return queryset

class CreateTicket(generics.CreateAPIView):
    serializer_class = CreateTicketSerializers

    def post(self, request, format=None):
        serializer = CreateTicketSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializers
    queryset = TicketOrder.objects.all()

class TicketVerification(generics.UpdateAPIView):
    serializer_class = VerificationSerializers

    def put(self, request, format=None):
        serializer = VerificationSerializers(data=request.data)
        if serializer.is_valid():
            ticketcode = TicketOrder.objects.filter(TicketCode=serializer.data['TicketCode']).update(Validation=1)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberList(generics.ListCreateAPIView):
    serializer_class = MemberSerializers
    queryset = Member.objects.all()

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializers
    queryset = Member.objects.all()
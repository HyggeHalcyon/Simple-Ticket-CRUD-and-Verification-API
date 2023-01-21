from rest_framework import serializers
from .models import TicketOrder, Member 

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = TicketOrder
        fields = ('__all__')

class CreateTicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = TicketOrder
        fields = ('Name', 'OrderType',)

class VerificationSerializers(serializers.ModelSerializer):
    TicketCode = serializers.CharField()

    class Meta:
        model = TicketOrder
        fields = ('TicketCode',)

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')

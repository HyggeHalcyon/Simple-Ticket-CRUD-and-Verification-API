from django.db import models
import uuid 

# Create your models here.

class Member(models.Model):
    MemberName = models.CharField(max_length=100, unique=True)    
    MemberPrice = models.IntegerField(unique=True)

    def __str__(self):
        return self.MemberName 

class TicketOrder(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(auto_now_add=True)
    TicketCode = models.CharField(max_length=5, unique=True)
    OrderType = models.ForeignKey(Member, on_delete=models.CASCADE)
    Validation = models.BooleanField(default=0)

    def save(self, force_insert=False, **kwargs):
        self.TicketCode = uuid.uuid4().hex[:5].upper()
        super(TicketOrder, self).save(force_insert=force_insert, **kwargs)

    def __str__(self):
        return self.Name
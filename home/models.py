from typing import Any
from django.db import models
from django.contrib.auth.models import User
class AuctionListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    auction_end = models.DateTimeField()
    auction_start = models.DateTimeField(null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionpicture = models.ImageField(default="goldpig.jpg",null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    highest_bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='highest_bids',blank=True)
    highest_bid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)

    def __str__(self):
      return self.title
    

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    auction_listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, null=True)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, editable=False , null=True)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)
    #def __str__(self):
     # return self.bidder.username
    #def __init__(self, *args, **kwargs):
       #super().__init__(*args, **kwargs)
       #if self.auction_listing:
      #  self.current_bid = self.auction_listing.current_bid
        #self.auction_name = self.auction_listing.title
     #  kwargs.setdefault('auction_listing', self.auction_listing)
    
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
      return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avail_bal = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    
    # Add fields for user profile details
    

class Feedback(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_given')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_received')
    feedback_text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
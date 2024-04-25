from typing import Any
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django import forms
from .models import *

class CreateUserForm(UserCreationForm): 
   class Meta: 
     model = User 
     fields = ['username', 'email', 'password1', 'password2'] 
     widget=forms.PasswordInput(attrs={'id': 'id_password'}) 

class BidForm(forms.ModelForm): 
   class Meta: 
     model = Bid
     fields = ['bid_amount'] 
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      if self.instance.auction_listing:
         self.fields['bid_amount'].label = f"{self.instance.auction_listing.title}-Current Bid:${self.instance.auction_listing.current_bid}"

   def save(self, commit=True):
      bid = super().save(commit=False)
      if commit:
         bid.save()

      if self.cleaned_data['bid_amount']:
         bid.bid_amount = self.cleaned_data['bid_amount']
         if bid.bid_amount > bid.auction_listing.current_bid:
            bid.auction_listing.current_bid = bid.bid_amount
            bid.auction_listing.highest_bidder = bid.bidder
            bid.auction_listing.highest_bid_amount = bid.bid_amount
            bid.auction_listing.save()
         else:
             raise forms.ValidationError("Bid amount must be greater than the current bid.")
          
      return bid         
   #    class BidForm(forms.ModelForm):
   #  class Meta:
   #      model = Bid
   #      fields = ['bid_amount']

   #  def __init__(self, *args, **kwargs):
   #      super().__init__(*args, **kwargs)

   #  def save(self, commit=True):
   #      bid = super().save(commit=False)
   #      if commit:
   #          bid.save()

   #      if self.cleaned_data['bid_amount']:
   #          bid_amount = self.cleaned_data['bid_amount']
   #          if bid_amount > bid.auction_listing.current_bid:
   #              bid.auction_listing.current_bid = bid_amount
   #              bid.auction_listing.highest_bidder = bid.bidder
   #              bid.auction_listing.highest_bid_amount = bid_amount
   #              bid.auction_listing.save()
   #          else:
   #             raise forms.ValidationError("Bid amount must be greater than the current bid.")
    
   #      return bid
 
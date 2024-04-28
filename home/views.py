from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm 
  
from django.contrib.auth.decorators import login_required ,user_passes_test 
from django.utils import timezone  
from django.contrib import messages 
from .models import AuctionListing, Bid
from .forms import CreateUserForm, BidForm
from .models import * 

from django.utils.html import strip_tags
  
from django.core.mail import send_mail 
from django.conf import settings 
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage,EmailMultiAlternatives 
  
from django.views.decorators.cache import never_cache 

 

def register(request): 
   if request.user.is_authenticated: 
     return redirect('home') 
   else: 
     form = CreateUserForm() 
     if request.method == 'POST': 
       form = CreateUserForm(request.POST) 
       if form.is_valid(): 
         form.save() 
         
         user = form.cleaned_data.get('username') 
         subject = f'AUCTIONG REGISTRATION' 
         message = 'Account Register Confirmation ' 
         recepiant = form.cleaned_data.get('email') 
         user = form.cleaned_data.get('username') 
         context ={ 
           'user' : user 
         
         } 
         card_html = render_to_string('registeremail.html', context) 
  
         email = EmailMultiAlternatives(subject, message,settings.EMAIL_HOST_USER, [recepiant]) 
  
         email.attach_alternative(card_html, 'text/html') 
         email.send(fail_silently=False) 
         messages.success(request,'Account created for '+ user) 

         return redirect('login') 
       return redirect('login')
  
   context ={ 'form' :form} 
  #  return render(request,'register.html', context) 
   return render(request,'register.html', context) 
  
 
 
 
 
 
def user_login(request): 
   if request.user.is_authenticated: 
     return redirect('home') 
   else: 
     if request.method == 'POST': 
       username = request.POST.get('username') 
       password = request.POST.get('password') 
       user = authenticate(request, username = username, password = password) 
       if user is not None: 
         login(request,user) 
         return redirect('home') 
       else: 
         messages.success(request,'Invalid Credential') 
         return render(request,'login.html') 
  
   context = {} 
   return render(request,'login.html', context) 
  
  
  
@login_required(login_url ='login') 
def logout_user(request):
    print("logout_user view was called")
    logout(request)
    return redirect('login')
   
  
  
@never_cache  
@login_required(login_url ='login')  
def index(request): 
  return render(request, 'home.html') 
  
  
@login_required(login_url ='login')    
def about(request): 
  return render(request, 'about.html') 
 
@never_cache
@login_required(login_url ='login')  
def contact(request): 
  return render(request, 'contact.html') 

@login_required(login_url ='login')  
def present(request): 
    auct = AuctionListing.objects.filter(auction_end__gt=timezone.now(), auction_start__lte=timezone.now())
    
    cont = {
    'auct': auct,
   

    
    }
    return render(request, 'present.html', cont) 

@login_required(login_url='login')
def auctions(request):
    acs = AuctionListing.objects.values('title', 'category', 'current_bid', 'auction_end', 'auctionpicture')
   
    con = {
        'auctions': acs,

    }
    return render(request, 'auctions.html', con)


@login_required(login_url ='login')  
def ongoing(request, auction_id): 
    auction = AuctionListing.objects.get(id=auction_id)
    default_image_url = '/static/img/goldpig.jpg'  # replace with the URL of your default image
    auction_picture_url = auction.auctionpicture.url if auction.auctionpicture else default_image_url
    context = {
      'title': auction.title,
      'desc': auction.description,
      'cat': auction.category,
      'curr': auction.current_bid,
      'auctionpicture': auction_picture_url,
      'auction': auction,
      'auction_id': auction_id,
      'seller': auction.seller,
      'start': auction.auction_start,
      'end': auction.auction_end,
      
      
     
    }
    return render(request, 'ongoing.html', context)

@login_required(login_url ='login')  
def upcoming(request): 
  return render(request, 'upcoming.html') 

@login_required(login_url ='login')  
def bids(request, auction_id): 
  form = BidForm()
  auction = get_object_or_404(AuctionListing, id=auction_id)
  if request.method == 'POST':
    form = BidForm(request.POST, instance=Bid(auction_listing=auction, bidder=request.user))
    if form.is_valid():
      form.save()
      return redirect('ongoing', auction_id=auction_id)
  else:
     form = BidForm(instance=Bid(auction_listing=auction, bidder=request.user))
  data = {
    'form':form,
    'auction':auction,
    'auction_title':auction.title,
    'auction_current_bid':auction.current_bid,
    'auction_seller':auction.seller,
  }
  return render(request, 'bidding.html', data)
# def bids(request, auction_id): 
#   form = BidForm()
#   auction = get_object_or_404(AuctionListing, id=auction_id)
#   if request.method == 'POST':
#     form = BidForm(request.POST)
#     if form.is_valid():
#       bid = form.save(commit=False)
#       bid.auction_listing = auction
#       bid.bidder = request.user
#       bid.save()
#       return redirect('ongoing', auction_id=auction_id)
#   else:
#     form = BidForm(initial={'auction_listing': auction, 'bidder': request.user})
#   data = {
#     'form':form,
#     'auction':auction,
#     'auction_title':auction.title,
#     'auction_current_bid':auction.current_bid,
#     'auction_seller':auction.seller,
#   }
#   return render(request, 'bidding.html', data)   
@login_required(login_url ='login')  
def history(request): 
  seller = request.user 
  user_history = AuctionListing.objects.filter(seller=seller)
  return render(request, 'history.html',{'history': user_history}) 
  #def myappointments(request):
   # user = request.user  # Assuming you are using Django's built-in User model
   # user_bookings = Booking.objects.filter(user=user)
   # return render(request, 'myappointments.html', {'bookings': user_bookings})
@login_required(login_url ='login')    
def profile(request): 
  return render(request, 'profile.html')
  
@login_required(login_url ='login')    
def win(request, auction_listing_id): 
    auction_listing = get_object_or_404(AuctionListing, id=auction_listing_id)

    # Check if the auction listing has ended and there is a highest bidder
    if auction_listing.auction_end < timezone.now() and auction_listing.highest_bidder:
        # Send an email to the highest bidder
        subject = f"You won the auction for {auction_listing.title}"
        html_message = render_to_string('email_template.html', {'auction_listing': auction_listing, 'bidder': auction_listing.highest_bidder})
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            'your_email@example.com',  # From email
            [auction_listing.highest_bidder.email],  # To email
            fail_silently=False,
            html_message=html_message
        )

    return render(request, 'winmail.html', {'auction_listing': auction_listing})
  


def is_admin(user): 
     return user.is_staff  # Assuming staff members are admins 
     
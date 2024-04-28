from . import views
from .views import Bid
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 
 
 path('',views.register, name ='register'), 
 path('home',views.index, name ='home'), 
 path('login',views.user_login, name ='login'), 
 path('about',views.about, name ='about'),
 path('contact',views.contact, name ='contact'),
 path('logout/', views.logout_user, name='logout_user'),
 path('ongoing/<int:auction_id>/',views.ongoing, name ='ongoing'), 
 path('upcoming',views.upcoming, name ='upcoming'),
 path('bid/<int:auction_id>/', views.bids, name='bids'),
 path('history',views.history, name ='history'),
 path('profile',views.profile, name ='profile'),
 path('present',views.present, name ='present'),
 path('auctions',views.auctions, name ='auctions'),
 
 
  
 path('reset_pass',auth_views.PasswordResetView.as_view(template_name = "passwordreset.html"), name='reset_password'), 
 path('reset_pass_sent',auth_views.PasswordResetDoneView.as_view(template_name = "passwordresetsent.html"), name='password_reset_done'), 
 
 path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "passwordresetform.html"), name='password_reset_confirm'), 


 path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="passwordresetdone.html"), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
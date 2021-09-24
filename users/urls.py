from django.urls import path
from users.views import EmailView, NameView, PasswordResetView,  SMSVerificationConfirmView, SMSVerificationView, SignupView, SigninView

urlpatterns = [ 
	path ('/signup', SignupView.as_view()),
	path ('/signin', SigninView.as_view()),
	path ('/email', EmailView.as_view()),
	path ('/sms', SMSVerificationView.as_view()),
	path ('/sms-verification', SMSVerificationConfirmView.as_view()),	
	path ('/reset', PasswordResetView.as_view()),	
	path ('/name', NameView.as_view()),	
] 


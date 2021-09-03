from django.urls import path

from makers.views import MakerView #OptionView 

urlpatterns = [
    path('', MakerView.as_view()),
    path('/<int:maker_id>',MakerView.as_view()),
    path('/draft/<int:maker_id>',MakerView.as_view()),
    #path('/option',OptionView.as_view()),
] 

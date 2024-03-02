"""
URL configuration for Respondr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MultiChannelIntegration.views import FacebookMessagesView
from MultiChannelIntegration.views import GmailMessagesView
from Authentication.views import signIn
from Authentication.views import signUp
from ModelIntegration.views import classifyText


urlpatterns = [
    path('admin/', admin.site.urls),
    path('facebook/messages/', FacebookMessagesView.as_view(), name='facebook_messages'),
    path('gmail/messages/', GmailMessagesView.as_view(), name='gmail_messages'),
    path('ai/model/classification', classifyText, name='messages_classification'),
    path('signIn/', signIn,name="signIn"),
    path('signUp/', signUp, name="signUp"),
]

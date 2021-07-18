from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.urls import reverse

from core.views import LoginGenericView, GenericView, LoginListView

# Create your views here.

class BaseRedirectView(RedirectView):

    def get_redirect_url(self, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return reverse('student:form')

        if user.is_authenticated:
            return reverse('account:dashboard')



class DefaultFormView(LoginGenericView):
    template_name = 'index.html'



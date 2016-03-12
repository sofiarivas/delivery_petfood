from django.shortcuts import render
from django.views.generic import View



# Create your views here.

class LoginView(View):
	def get(self, request):
		template_name = "login/login.html"
		return render(request, template_name)


# Create your views here.

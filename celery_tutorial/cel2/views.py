from django.shortcuts import render, HttpResponse
from cel2.forms import *
from django.views.generic.edit import FormView
# Create your views here.

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = Review
    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for your review!"
        return HttpResponse(msg)


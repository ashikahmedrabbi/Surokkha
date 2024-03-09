from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .models import vaccines
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from doctor.models import Doctor
from .models import borrow

@method_decorator(login_required, name='dispatch')
class AddVaccines(CreateView):
    model = models.vaccines
    form_class = forms.vaccinesForm
    template_name = 'add_vaccines.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.Doctor = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditVaccines(UpdateView):
    model = models.vaccines
    form_class = forms.vaccinesForm
    template_name = 'add_vaccines.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@method_decorator(login_required, name='dispatch')
class delete_vaccines(View):
    def get(self, request, id):
        vaccines_instance = models.vaccines.objects.get(pk=id)
        vaccines_instance.delete()
        return redirect('profile')

def vaccines_list(request):
    
    doctor = Doctor.objects.get(user=request.user)

    # Filter vaccines based on the associated doctor
    vaccines_data = vaccines.objects.filter(doctor=doctor)
    
    data_with_images = [item for item in vaccines_data if item.image]
    return render(request, 'vaccines.html', {'data': data_with_images})

def patients_vaccines_list(request):
    vaccines_data = vaccines.objects.all()
    data_with_images = [item for item in vaccines_data if item.image]
    return render(request, 'patientsvaccines.html', {'data': data_with_images})



class Detailvaccines(LoginRequiredMixin,DetailView):
    model = models.vaccines
    pk_url_kwarg = 'id'
    template_name = 'details.html'

    def post(self, request, *args, **kwargs):
        reviews_form = forms.reviewsForm(data=request.POST)
        vaccines = self.get_object()

        if reviews_form.is_valid():
            new_review = reviews_form.save(commit=False)
            new_review.vaccines = vaccines
            new_review.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vaccines = self.object 
        reviews = vaccines.reviews.all()
        reviews_form = forms.reviewsForm()

        UserAccount = self.request.user.account
        has_borrowed = models.borrow.objects.filter(user=UserAccount, Vaccines=vaccines).exists()
        context['reviews'] = reviews

        context['reviews_form'] = reviews_form
        context['has_borrowed'] = has_borrowed

        return context

    def get_form(self):
        return self.form_class(data=self.request.POST or None)
    


        

@method_decorator(login_required, name='dispatch')
class BorrowvaccinesList(ListView):
    model = borrow
    template_name = 'vaccinebooking.html'
    context_object_name = 'borrowed_vaccines'

    def get_queryset(self):
        # Assuming that each user can have multiple borrow entries
        queryset = borrow.objects.filter(user=self.request.user.account)
        return queryset

@method_decorator(login_required, name='dispatch')   
class borrow_vaccines(LoginRequiredMixin, View):

    def get(self, request, id, **kwargs):
        vaccine = get_object_or_404(vaccines, id=id)
        user = self.request.user

        try:
            # Try to create a new borrow record
            new_borrow = borrow.objects.create(user=user.account, Vaccines=vaccine)
            messages.success(request, f'You have successfully borrowed {vaccine.name}.')
        except Exception as e:
            # Handle the exception (e.g., IntegrityError if the record already exists)
            messages.warning(request, f'Failed to borrow {vaccine.name}. {e}')

        return redirect('home')


       
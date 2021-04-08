from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

import datetime

from app.models.samples import Sample,SampleRequest
from app.forms.sample_form import SampleRequestForm, SampleForm
from app.selectors.sample_selector import (
    get_sample_requests, 
    get_sample_request,
    get_samples_on_request,
    generate_auto_number,
)

     
def manage_sample_requests(request):
    
    auto_no = generate_auto_number()
    year = datetime.datetime.today().year
    request_no = f"MEMD/LAB/RAF/{year}/{auto_no}"
    
    request_form = SampleRequestForm(initial={"reg_no":request_no})
    requests = get_sample_requests()
    
    if request.method == "POST":
        request_form = SampleRequestForm(request.POST, request.FILES)
        if request_form.is_valid():
            request_form.save()
            messages.success(request, 'Sample Request Record saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
         
    context = {
        "request_form": request_form,
        "requests": requests
    }
    return render(request, "quality_assurance/manage_sample_requests.html", context)

def manage_samples(request, sample_request_id):
    
    sample_request = get_sample_request(sample_request_id)
    
    sample_form = SampleForm(initial={"sample_request":sample_request})
    
    samples = get_samples_on_request(sample_request)
    
    if request.method == "POST":
        sample_form = SampleForm(request.POST, request.FILES)
        
        if sample_form.is_valid():
            sample_form.save()
            messages.success(request, 'Sample Record saved Successfully!')
            
        else:
            messages.warning(request, 'Operation Not Successfull')
            
        return HttpResponseRedirect(reverse(manage_samples,args=[sample_request_id]))
         
    context = {
        "sample_form": sample_form,
        "samples": samples
    }
    return render(request, "quality_assurance/manage_samples.html", context)



    
    
        
    




  

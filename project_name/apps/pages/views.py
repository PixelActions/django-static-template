from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from django import forms

class ContactForm(forms.Form):
    city = forms.CharField(max_length=100, required=True)
    name = forms.CharField(max_length=100, required=True)
    sender = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=100, required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)
    cc_myself = forms.BooleanField(required=False)
    
class AboutView(TemplateView):
    template_name = "pages/about.html"
    
def contact(request):
    context = {}
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            city = form.cleaned_data['city']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            telephone = form.cleaned_data['telephone']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['info@pixelactions.com']
            if cc_myself:
                recipients.append(sender)

            subject = name + ' from ' + city
            comment = "[TEL:" + telephone + "]\n" + comment
            
            from django.core.mail import send_mail
            send_mail(subject, comment, sender, recipients)
            
            context['formsuccess'] = True
            form = ContactForm() # An unbound form
            #return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    context['form']= form
    
    return render(request, 'pages/contact.html', context)

class TermsView(TemplateView):
    template_name = "pages/terms.html"
class DisclaimerView(TemplateView):
    template_name = "pages/disclaimer.html"
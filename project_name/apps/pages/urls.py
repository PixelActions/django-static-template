from django.conf.urls import patterns, include, url
from .views import AboutView, TermsView, DisclaimerView, contact

urlpatterns = patterns('',
   url(r'^about/$', AboutView.as_view(), name='pages_about'),
   url(r'^terms/$', TermsView.as_view(), name='pages_terms'),
   url(r'^disclaimer/$', DisclaimerView.as_view(), name='pages_disclaimer'),
   url(r'^contact/$',contact, name='pages_contact'),
)

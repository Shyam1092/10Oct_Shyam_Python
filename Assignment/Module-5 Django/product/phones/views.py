from django.shortcuts import render

from .models import PhoneCompany, Phone

def index(request):
    companies = PhoneCompany.objects.all()
    return render(request, 'index.html', {'companies': companies})

def company_detail(request, company_name):
    company = PhoneCompany.objects.get(name=company_name)
    phones = company.phones.all()
    return render(request, 'company_detail.html', {'company_name': company_name, 'phones': phones})

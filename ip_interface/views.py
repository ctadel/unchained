import json
from django.shortcuts import render
from django.views import View
from .models import IP_Records
from django.http import JsonResponse, HttpResponse


# Create your views here.
class IP_Interface(View):
    def get(self,request):
        context = {'title':'ctadel | Home Server'}
        latest_record = IP_Records.objects.values().order_by('-id')[:1]
        if latest_record:
            context['ip'] = latest_record[0]
        return render(request,"ip_interface/index.html",{'context':context})

    def post(self,request):
        latest_record = IP_Records.objects.values().order_by('-id')[:1][0]
        json_data = json.dumps(latest_record, indent=4, sort_keys=True, default=str)
        return JsonResponse(json_data,safe=False)

class IP_Listing(View):
    def get(self,request):
        records = IP_Records.objects.values().order_by('-id')
        context = {'title':'ctadel | IP Listing'}
        context['records'] = records
        return render(request,"ip_interface/listing.html",{'context':context})

from django.shortcuts import render
from slmsapp.models import Staff, Staff_Leave

def FIRSTPAGE(request):
    empcount = Staff.objects.count()
    dptcount = 0   # you can update later if you have department model
    leavtypcount = Staff_Leave.objects.count()

    results = Staff_Leave.objects.all().order_by('-id')[:5]

    return render(request, 'index.html', {
        'empcount': empcount,
        'dptcount': dptcount,
        'leavtypcount': leavtypcount,
        'results': results
    })

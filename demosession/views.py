from django.shortcuts import render,redirect

# Create your views here.
def view_visitor_count(request):
    count = request.session.get('count','NA')
    if count == 'NA':
        count=1
    else:
        count=count+1
    request.session['count']=count
    d1={'count':count}
    return render(request,'demosession/count.html',context=d1)


def view_write_cookie(request):
    if request.method == 'GET':
        return render(request,'demosession/write.html')
    elif request.method == 'POST':
        name = request.POST.get('txtname','NA')
        resp= render(request,'demosession/write.html')
        resp.set_cookie(key='abc',value=name,max_age=60*60*24*365)
        return resp



def view_read_cookie(request):
    if request.method == 'GET':
        return render(request,'demosession/read.html')
    elif request.method == 'POST':
        name =request.COOKIES.get('abc','NA')
        if name == 'NA':
            data ={'name':'cookies not found'}
        else:
            data = {'name':name}
        resp= render(request,'demosession/read.html',context=data)
        return resp

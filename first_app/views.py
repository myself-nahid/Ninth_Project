from django.shortcuts import render

# Create your views here.

def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'Nahid', max_age=10)
    # response.set_cookie('name', 'Hasan')
    return response
def get_cookies(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'del_cookie.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {
        'name' : 'Nahid',
        'age' : 23,
        'language' : 'Bangla'
    }
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    name = request.session.get('name', 'Guest')
    age = request.session.get('age')
    return render(request, 'get_session.html' , {'name': name, 'age': age})

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request, 'del_cookie.html')
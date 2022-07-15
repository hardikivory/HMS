

from tabnanny import check
from django.shortcuts import redirect, render, HttpResponse
from requests import delete, request

from .forms import ChangePasswordForm, ContactForm, GuestUpdateForm, UserRegisterForm, UserLoginForm, WorkerUpdateForm, RoomForm
from . models import User, Guest, Worker, Room
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import os

from django.core.mail import EmailMessage
# Create your views here.


def my_login_required(function):
    def wrapper(request, *args, **kw):
        try:
            user = Guest.objects.get(username=request.session.get('user'))
        except:
            user = True

        if not (user and request.session.get('user')):
            return HttpResponseRedirect('/accounts/login/')
        else:
            return function(request, *args, **kw)
    return wrapper


def NavView(request):
    my_id = request.session.get('user')
    print(my_id)
    print(type(my_id))
    try:
        try:
            guest = Guest.objects.get(username=my_id)
            check_guest = guest.id
            print(type(check_guest))
            check_worker = None
            print('Guest: ', check_guest)
        except:
            worker = Worker.objects.get(username=my_id)
            check_worker = worker.id
            print(type(check_worker))
            check_guest = None
            print('Worker: ', check_worker)

    except:
        print('Guest ID does not exist..')
        print('Worker ID does not exist...')
        check_guest = None
        check_worker = None

    return render(request, 'nav.html', {'guest': check_guest, 'worker': check_worker})


def HomeView(request):
    my_id = request.session.get('user')
    print(my_id)
    print(type(my_id))
    try:
        try:
            guest = Guest.objects.get(username=my_id)
            check_guest = guest.id
            print(type(check_guest))
            check_worker = None
            print('Guest: ', check_guest)
        except:
            worker = Worker.objects.get(username=my_id)
            check_worker = worker.id
            print(type(check_worker))
            check_guest = None
            print('Worker: ', check_worker)
    except:
        check_guest = None
        check_worker = None
        print('Guest ID does not exist...')
        print('Worker ID does not exist...')

    return render(request, 'home.html', {'guest': check_guest, 'worker': check_worker})


def RegisterView(request):
    if request.method == 'POST':
        fm = UserRegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            username = fm.cleaned_data.get('username')
            email = fm.cleaned_data.get('email')
            email = email.lower()
            print(username)

            temp_pass = User.objects.get(username = username)
            temp_pass = temp_pass.password
            print('TEMP_PASS: ',temp_pass)
            subject = 'HMS REGISTATION'
            
            message = f""" Hello,{username} \n 
            Your Username: {username} 
            Temporary Password: {temp_pass}
            Please change your password...
           """
            
            from_email = 'hardik1.ivorytechnolab@gmail.com'
            to_email = email
            print(to_email)
            
            
            data = {
                'subject' : subject,
                'message' : message,
                'from_email' : from_email,
                'to_email' : to_email,
            }
            
            
            #email
            def send_email(data):
                email = EmailMessage(
                    subject= data['subject'],
                    body= data['message'],
                    from_email= data['from_email'],
                    to= [data['to_email']],
                )
                email.send()
                if email.send():
                    print('Mail sent....')
                    
                
            send_email(data)
            return redirect('login')
        else:
            print('REGISTASTION FAILED....')

    fm = UserRegisterForm()
    return render(request, 'register.html', {'form': fm})


def LoginView(request):
    if request.method == 'POST':
        fm = UserLoginForm(request.POST)
        if fm.is_valid():

            request.session['user'] = fm.cleaned_data.get('username')
            print('LOGIN SUCCESSFULLY....')
            return redirect('home')
        else:

            print('LOGIN FAILED....')

    fm = UserLoginForm()

    return render(request, 'login.html', {'form': fm})



@my_login_required
def LogoutView(request):
    print('LOGOUT...')
    request.session.flush()
    return redirect('login')



@my_login_required
def GuestChangePasswordLinkView(request):
    
    subject = 'HMS Change Password'
    
    message = '''Click on link for Changing Password \n
    http://127.0.0.1:8000/accounts/changepassword/
    \n'''
    
    from_email = 'hardik1.ivorytechnolab@gmail.com'
    try:
        user = Guest.objects.get(username = request.session.get('user'))
        email = user.email
        email = email.lower()
        to_email = email
        
        data = {
                    'subject' : subject,
                    'message' : message,
                    'from_email' : from_email,
                    'to_email' : to_email,
                }
                
                
        #email
        def send_email(data):
            email = EmailMessage(
                subject= data['subject'],
                body= data['message'],
                from_email= data['from_email'],
                to= [data['to_email']],
                    )
            email.send()
            if email.send():
                print('Mail sent....')
            
                    
        send_email(data)
    except:
        print('ID Does not Exist...')
    return render(request, 'guestdashboard.html')


@my_login_required
def GuestChangePasswordView(request):
    fm = ChangePasswordForm(request.POST)
    if True:
        user = request.session.get('user')
        try:
            check_user = Guest.objects.get(username = user)
            
            old_pass = request.POST.get('old_password')
            new_pass = request.POST.get('new_password')
            print('OLD_PASS: ',old_pass)
            print('NEW_PASS: ',new_pass)
            if old_pass == check_user.password and len(new_pass) <= 8:
                
                check_user.password = new_pass
                
                try:
                    check_user.save()
            
                except:
                    print('PAssword not Change...')
                
                request.session.flush()
                print('Password Change Successfully...')
                return redirect('login')       
            
            else:
                print('PASSWORD NOT CHANGED...')
                print('PASSWORD MAXIMUM 8 CHARACTER...')
        except:
            print('ID Does not Exist....')
            return redirect('login')     
    fm = ChangePasswordForm()
    return render(request, 'changepassword.html', {'form': fm})



@my_login_required
def GuestDashboardView(request):
    my_id = request.session.get('user')
    print(my_id)
    print(type(my_id))
    try:
        guest = Guest.objects.get(username=my_id)
        check_guest = guest.id

        print(type(check_guest))
        print(check_guest)
        print(guest.profile_pic)

        try:
            check_room = guest.room_no.room_no
            print(check_room)
            print('WELCOME TO THE DASHBOARD....')
        except:
            check_room = None
    except:
        print('ID DOES NOT EXIST..')
        check_guest = None
        guest = None
        check_room = None
    return render(request, 'guestdashboard.html', {'guest': check_guest, 'data': guest, 'check_room': check_room, 'photo': guest.profile_pic})


@my_login_required
def GuestUpdateView(request, id):

    if request.method == 'POST':
        # print(type(id))
        update_data = User.objects.get(id=id)
        post_data = request.POST or None
        file_data = request.FILES or None
        print(update_data.profile_pic)
        
            
        # user_form = GuestUpdate1Form(post_data, instance = update_data)
        profile_form = GuestUpdateForm(
            post_data, file_data, instance=update_data)

        if profile_form.is_valid():

            profile_form.save()
            print('profile updated...')
            return redirect('home')

    fm = GuestUpdateForm()

    return render(request, 'guestupdate.html', {'form': fm})


@login_required
def GuestDeleteView(request):
    my_id = request.session.get('user')
    try:
        guest = Guest.objects.get(username=my_id)
        print(guest)
        check_guest = guest.id
        print('check', check_guest)

        delete_guest = Guest.objects.get(username=my_id)
        delete_guest.delete()
        request.session.flush()
        print('GUEST ACCOUNT DELETED...')
    except:
        print('ID DOES NOT EXIST...')
    return render(request, 'home.html')



# WORKER
@my_login_required
def WorkerChangePasswordLinkView(request):
    
    subject = 'HMS Change Password'
    
    message = '''Click on link for Changing Password \n
    http://127.0.0.1:8000/accounts/worker/changepassword/
    \n'''
    
    from_email = 'hardik1.ivorytechnolab@gmail.com'
    try:
        user = Guest.objects.get(username = request.session.get('user'))
        email = user.email
        email = email.lower()
        to_email = email
        
        data = {
                    'subject' : subject,
                    'message' : message,
                    'from_email' : from_email,
                    'to_email' : to_email,
                }
                
                
        #email
        def send_email(data):
            email = EmailMessage(
                subject= data['subject'],
                body= data['message'],
                from_email= data['from_email'],
                to= [data['to_email']],
                    )
            email.send()
            if email.send():
                print('Mail sent....')
            
                    
        send_email(data)
    except:
        print('ID Does not Exist...')
    return render(request, 'workerdashboard.html')


@my_login_required
def WorkerChangePasswordView(request):
    fm = ChangePasswordForm(request.POST)
    if True:
        user = request.session.get('user')
        try:
            check_user = Worker.objects.get(username = user)
            
            old_pass = request.POST.get('old_password')
            new_pass = request.POST.get('new_password')
            print('OLD_PASS: ',old_pass)
            print('NEW_PASS: ',new_pass)
            if old_pass == check_user.password and len(new_pass) <= 8:
                
                check_user.password = new_pass
                
                try:
                    check_user.save()
            
                except:
                    print('Password not Change...')
                
                request.session.flush()
                print('Password Change Successfully...')
                return redirect('login')       
            
            else:
                print('PASSWORD NOT CHANGED...')
                print('PASSWORD MAXIMUM 8 CHARACTER...')
        except:
            print('ID Does not Exist....')
            return redirect('login')     
    fm = ChangePasswordForm()
    return render(request, 'changepassword.html', {'form': fm})




@my_login_required
def WorkerDashboardView(request):
    my_id = request.session.get('user')
    print(my_id)
    print(type(my_id))
    try:
        worker = Worker.objects.get(username=my_id)
        check_worker = worker.id
        print(type(check_worker))
        
        print(check_worker)
        print(worker.profile_pic)
        print('WELCOME TO THE WORKER DASHBOARD....')
       
    except:
        print('ID DOES NOT EXIST..')
        check_worker = None
        worker = None
    
    return render(request, 'workerdashboard.html', {'worker': check_worker, 'data': worker, 'photo': worker.profile_pic})


@login_required
def WorkerUpdateView(request, id):

    if request.method == 'POST':
        # print(type(id))
        update_data = User.objects.get(id=id)
        post_data = request.POST or None
        file_data = request.FILES or None
        print(update_data.profile_pic)
        
            
        # user_form = GuestUpdate1Form(post_data, instance = update_data)
        profile_form = WorkerUpdateForm(
            post_data, file_data, instance=update_data)

        if profile_form.is_valid():

            profile_form.save()
            print('profile updated...')
            return redirect('home')

    fm = WorkerUpdateForm()
    
    return render(request, 'workerupdate.html', {'form': fm})


@login_required
def WorkerDeleteView(request):
    my_id = request.session.get('user')
    try:
        worker = Worker.objects.get(username=my_id)
        print(worker)
        check_worker = worker.id
        print('check', check_worker)

        delete_worker = Worker.objects.get(username=my_id)
        delete_worker.delete()
        request.session.flush()
        print('WORKER ACCOUNT DELETED...')
    except:
        pass
    return render(request, 'home.html')


@my_login_required
def RoomView(request):
    try:
        my_id = request.session.get('user')
        guest = Guest.objects.get(username=my_id)
        print(guest)
        check_guest = guest.id
        print('check', check_guest)

        user = Guest.objects.get(username=request.session.get('user'))
    except:
        user = False
        print('USER NOT LOGIN....')
    if user:
        if request.method == 'POST':
            fm = RoomForm(request.POST)
            if fm.is_valid():
                rm_type = fm.cleaned_data.get('room_type')
                print((rm_type))

                type_room = Room.objects.filter(room_type=rm_type)
                ttl_guest = Room.objects.filter(
                    room_type=rm_type).values_list('room_guest')
                available_guest = []
                for i in ttl_guest:

                    available_guest.append(5 - int(i[0]))

                print('available_guest: ', available_guest)

                print('type_room: ', type_room)
                print('SHOW ALL THE AVAILABLE ROOMS....')
                temp = False
                dict = {
                    'form': fm,
                    'temp': temp,
                    'available_guest': available_guest,
                    'type_room': type_room,
                }
                return render(request, 'room.html', dict)
    else:
        print('GUEST ID DOES NOT EXIST...')
        return redirect('login')

    fm = RoomForm()
    temp = True
    dict = {
        'form': fm,
        'temp': temp,
    }
    return render(request, 'room.html', dict)


@my_login_required
def RoomBookView(request, room_no):
    try:
        my_id = request.session.get('user')
        guest = Guest.objects.get(username=my_id)
        print(guest)
        check_guest = guest.id
        print('check', check_guest)

        check_room = Room.objects.get(room_no=room_no)
        check_room_price = check_room.room_type.my_room_price
        print(check_room)
        print(type(check_room))
        print('PRICE: ', check_room_price)

        empty_room = Guest.objects.get(username=my_id)
        check_free_room = empty_room.room_no

        if check_free_room:
            print('ROOM ALREADY ASIGNED....')
        else:
            book_room = Guest.objects.update(
                room_no=check_room, fees=check_room_price)
            book_room.save()
            print('ROOM BOOK SUCCESSFULLY...')

            return redirect('home')

        dict = {
            'check_guest': check_guest,
            'check_free_room': check_free_room
        }

    except:
        check_guest = None
        print('GUEST ID DOES NOT EXIST....')

        dict = {
            'check_guest': check_guest
        }
    return render(request, 'roombook.html', dict)


def FeesView(request):

    try:
        my_id = request.session.get('user')
        guest = Guest.objects.get(username=my_id)
        print(guest)
        check_guest = guest.id
        print('check', check_guest)

        room_no = guest.room_no.room_no
        print(room_no)
        print(type(room_no))
        check_status = guest.status
        print(check_status)
        print(type(check_status))
        update_status = Guest.objects.update(status='SUCCESS')
        update_status.save()
        print(update_status)
        print('FEES PAY SUCCESSFULLY...')
        print('STATUS UPDATED...')
        dict = {
            'check_guest': check_guest
        }

    except:
        check_guest = None
        print('GUEST ID DOES NOT EXIST...')
        dict = {
            'check_guest': check_guest
        }
    return render(request, 'home.html', dict)


def AboutView(request):
    return render(request, 'about.html')


def ContactView(request):

    fm = ContactForm(request.POST)
    if fm.is_valid():
        fm.save()
        print('CONTACT FORM SEND SUCCESSFULLY....')
        return redirect('home')
    else:
        print('INVALID FORM...')

    fm = ContactForm()
    return render(request, 'contact.html', {'form': fm})

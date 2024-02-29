#from app1.forms import RegistrationForm
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from app1.models import Registration,validate_mail
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
import smtplib
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse


# # Create your views here.
# def home(request):
#     return redirect('registration')
def registartion(request):
    return render(request,'registration.html')
def create_daata(request):
    if request.method == "POST":
        name = request.POST['name']
        sur_name = request.POST['sur_name']
        mobile= request.POST['mobile_number']
        print(f"THIS IS mobile {mobile}")
        try:
            email = validate_mail(request.POST['email'])
            print(f"THIS IS EMI {email}")
        except ValidationError as e:
            error_message = str(e)
            return render(request,'registration.html',{'error_message':error_message})

        age = request.POST['age']
        occupation = request.POST['occupation']
        #image = request.FILES.get('image')
        obj = Registration.objects.create(name=name, sur_name = sur_name,mobile= mobile,email = email,age=age, occupation = occupation)
        obj.save()
        return redirect('/')
    return redirect('registartion/')
def retrieve(request):
    details=Registration.objects.all()
    # paginator = Paginator(details, 2)  # Create a Paginator instance with 25 items per page
    # page_number = request.GET.get('page')  # Get the current page number from the GET parameters
    # page_obj = paginator.get_page(page_number)
    # context = {
    #     'page_obj': page_obj,  # Pass the Page object to the template context
    #     'base_url': reverse('retrieve'),  # Get the base URL for the current view
    # }
    return render(request,'view_data.html', {"details":details})
 
def my_view_redirect(request):
    # Redirect to the first page of the paginated view
    return redirect(reverse('retrieve') + '?page=1')


def edit(request, id):
    print(id)
    object = Registration.objects.get(id=id)
    print(object.name)
    return render(request, 'edit.html', {'object': object})


def update(request, id):
    object = get_object_or_404(Registration, id=id)
    if request.method == 'POST':
        object.name = request.POST.get('name')
        object.sur_name = request.POST.get('sur_name')
        object.mobile = request.POST.get('mobile')
        object.email = request.POST.get('email')
        object.age = request.POST.get('age')
        object.occupation = request.POST.get('occupation')
        object.save()
        return redirect('retrieve')
    else:
        return render(request, 'view_data.html', {'object': object})

def delete(request, pk):
    Registration.objects.filter(id=pk).delete()
    return redirect('retrieve')

# def email_send(request,id):
#     object = Registration.objects.filter(id =id)
#
#     recipient_email = object.email
#     object_data = [
#         f"Name: {object.name}",
#         f"Surname: {object.sur_name}",
#         f"Mobile Number: {object.mobile}",
#         f"Email: {object.email}",
#         f"Age: {object.age}",
#         f"Occupation: {object.occupation}"
#     ]
#     subject = 'Your Details in DB'
#     message = "\n".join([f"• {data}" for data in object_data])
#     from_email = settings.EMAIL_HOST_USER
#     res = send_mail(subject,message,from_email,recipient_list=[recipient_email],fail_silently=False)
#     return redirect('retrieve')
# def email_send(request,pk):
#     object = Registration.objects.get(id = pk)
#
#     recipient_email = object.email
#     object_data = [object.name, object.sur_name, object.mobile, object.email, object.age, object.occupation]
#     subject = 'Your Details in DB'
#     message = f'The following fields were the details in our db: '
#     #from_email = settings.EMAIL_HOST_USER
#     send_mail(subject, message, from_email = 'klakshmireddy939@gmail.com', recipient_email = [recipient_email], fail_silently=False)
#     return redirect('retrieve')

def email_send(request,id):
    print("Mail_function")
    object = Registration.objects.get(id =id )

    recipient_email = object.email
    #object_data = [object.name, object.sur_name, str(object.mobile), object.email, str(object.age), object.occupation]
    object_data = [
                f"Name: {object.name}",
              f"Surname: {object.sur_name}",
                f"Mobile Number: {object.mobile}",
               f"Email: {object.email}",
                 f"Age: {object.age}",
                f"Occupation: {object.occupation}"
           ]
    subject = 'Your Details in DB'
    new_line = '\n'
    message = f'The following fields were the details in our db:{new_line} {new_line.join(object_data)}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = recipient_email
    try:
        send_mail(subject, message, from_email, [recipient_list], fail_silently=False)
    except smtplib.SMTPAuthenticationError as e:
        error_message = str(e) + f' /n Email uthentication was failed please check your mail is {from_email},set app to less secure so it will wor'
        return render(request, 'status.html', {'error_message': error_message})
    messages.success(request, "Details are sent. press home button to back homepage")

    return render(request,'status.html')
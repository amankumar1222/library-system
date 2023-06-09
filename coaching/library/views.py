from django.shortcuts import render , redirect ,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import logout, login , authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Seat

# Create your views here.

def index(request):
   
    username = request.user.username
    print(username)
    # allSeats = objects.all()
    # n = len(allSeats)
    

    available_seats = Seat.objects.filter(is_booked=False)
    seats = Seat.objects.all()
    params = {"seats":available_seats, "tseats":seats}
    return render(request,"library/index.html", params)

    



# this is signUp form and i will not touch this form 
def singupuser(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username)<10:
            messages.error(request, "Your user name must be under 10 characters")
            return redirect('/login')
        if not username.isalnum():
            messages.error(request, "User name should only contain letter and numbers")
            return redirect('/')
        if (pass1 != pass2):
            messages.error(request, "Password do not match")
            return redirect("/login")



        # Create the user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Successfully logged out")
        return redirect('/')
    

    return render(request, 'singupuser.html')

# here logout form and i will not touch this form
def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/library/login/')

# here login form and i will not tocuh this form
def loginuser(request,seat=""):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Successfully Logged In {seat}")
            return redirect("/library")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return render(request, 'loginuser.html')


# here book seat is main things for me 
def BookSeats(request):
    # username = request.user.username
    seats = Seat.objects.all()
    if request.user.is_anonymous:
        return redirect("/library/login/")
    if request.method == "POST":
        seat_number = int(request.POST['seat_number'])
        name = request.POST['name']
        gender = request.POST['gender']
        username = request.POST['username']
          # Check if the user has already booked a seat
        if username == request.user.username:
            print("success")
            if Seat.objects.filter(myuser=request.user.username).exists():
                return redirect('already_booked')  # Redirect to a page indicating that the user has already booked a seat
        seat = Seat.objects.get(seat_number=seat_number)
        seat.is_booked = True
        seat.name = name
        seat.gender = gender
        seat.save()
        messages.success(request, f"Your Seat has been Booked")
        return redirect('/library/')


    context = {'seats': seats,}
    return render(request,"library/booking.html",context)
    


def cancelSeats(request, seat):
    seat = Seat.objects.get(seat_number=seat)
    seat.name =""
    seat.gender =""
    seat.is_booked = False
    seat.save() 
    messages.success(request, f"Your Seat {seat} has been canceled ")
    return redirect('/library')


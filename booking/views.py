from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from booking.models import Movie

# View for booking a movie

def book_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)  # Fetch the movie based on ID
    return render(request, 'booking/book_ticket.html', {'movie': movie})

# Home view
def home(request):
    return render(request, 'booking/home.html')

# View to list movies
def movie_view(request):
    return render(request, 'booking/movies.html')

# View for booking ticket (with POST handling)






def book_ticket(request, movie_id):
    if request.method == 'POST':
        # Add booking logic here
        return redirect('booking_success')  # Redirect to a success page
    return render(request, 'booking/book_ticket.html', {'movie_id': movie_id})

# View for movie details
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

# View for searching movies
def search(request):
    query = request.GET.get('q')
    movies = Movie.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'movies': movies})

# User signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# User registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to home page after successful registration
    else:
        initial_data = {'username': '', 'password1': '', 'password2': ''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'booking/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get the cleaned data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log in the user
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        initial_data = {'username': '', 'password': ''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'booking/login.html', {'form': form})

# Dashboard view (currently does nothing)
def dashboard(request):
    pass

# User logout view
def logout_view(request):
    auth_logout(request) 
    return redirect('login')  # Redirect to login page after logout







def payment(request):
    show_time = request.GET.get('time', 'Not specified')
    selected_seats = request.GET.get('seats', 'None')
    show_date = request.GET.get('date', 'Not specified')
    
    context = {
        'show_time': show_time,
        'selected_seats': selected_seats,
        'show_date': show_date
    }
    return render(request, 'booking/payment.html', context)
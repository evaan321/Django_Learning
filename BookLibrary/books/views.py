from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *
from .forms import *
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMessage
from django.contrib import messages



from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'Home.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['data']= Book.objects.all()
        return context
    
def Home(request):
    return render(request, 'Home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    def get_success_url(self) -> str:
        return reverse_lazy('home')

class CustomRegisterView(CreateView):
    template_name = 'register.html'
    form_class =    RegisterForm
    
    success_url = reverse_lazy('login')
    

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        subject = 'Welcome to Our Library'
        message = f"Thank you {form.cleaned_data['username']} for registering on Our Library. We hope you enjoy your experience!"
        from_email = 'evaanrahman2@gmail.com'  
        to_email = [form.cleaned_data['email']]  

        email = EmailMessage(subject, message, from_email, to_email)
        email.send()
        return redirect('login')
    
class HomeView(TemplateView):
    template_name = 'Home.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        if user.is_authenticated:
            try:
                user_model = UserModel.objects.get(user=user)
            except UserModel.DoesNotExist:
                user_model = UserModel.objects.create(user=user, balance=0)
        else:
            
            user_model = None

        context['data'] = Book.objects.all()
        context['count'] = Book.objects.all().count()
        context['categories'] = [
            ('Horror', 'Horror'),
            ('Fiction', 'Fiction'),
            ('Novel', 'Novel'),
            ('Fantasy', 'Fantasy'),
            ('Story', 'Story')
        ]
        context['myUser'] = user_model
        return context

class CategoryView(ListView):
    model = Book
    template_name = 'Home.html'  
    context_object_name = 'data'

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category:
            return Book.objects.filter(category=category)
        return Book.objects.all()

    

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['reviews'] = BookReview.objects.filter(book=self.object)
        return context


@login_required
def deposit_money(request):
    user = request.user
    try:
        user_model = UserModel.objects.get(user=user)
    except UserModel.DoesNotExist:
        
        user_model = UserModel.objects.create(user=user, balance=0)

    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_model.balance += amount
            user_model.save()
            subject = 'Welcome to Our Library'
            message = f"Thank you for Depositing {form.cleaned_data['amount']} Taka on Our Library . We hope you Keep Depositing more money !"
            from_email = 'evaanrahman2@gmail.com'  
            to_email = [request.user.email]  

            email = EmailMessage(subject, message, from_email, to_email)
            email.send()
            

            

            messages.success(request, 'Money deposited successfully.')
            return redirect('home')
    else:
        form = DepositForm()

    return render(request, 'deposit.html', {'form': form,'data':user_model})

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user_model = UserModel.objects.get(user=request.user)

    if user_model.balance >= book.bPrice:
        
        borrowed_book = BorrowedBook.objects.create(user=request.user, book=book)

        
        user_model.balance -= book.bPrice
        user_model.save()

        

        messages.success(request, f'Book "{book.title}" borrowed successfully.')
    else:
        messages.error(request, 'Insufficient funds to borrow the book.')

    return redirect('home')

@login_required
def profile(request):
    user_model = UserModel.objects.get(user=request.user)
    borrowed_books = BorrowedBook.objects.filter(user=request.user)

    return render(request, 'profile.html', {'user_model': user_model, 'borrowed_books': borrowed_books})

@login_required
def review_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            messages.success(request, 'Review submitted successfully.')
            return redirect('home')  
    else:
        form = ReviewForm()

    return render(request, 'review_book.html', {'form': form, 'book': book})

@login_required
def return_book(request, borrowed_book_id):
    borrowed_book = BorrowedBook.objects.get(pk=borrowed_book_id)

    if not borrowed_book.returned:
        
        borrowed_book.returned = True
        
        borrowed_book.save()

        user_model = UserModel.objects.get(user=request.user)
        user_model.balance += borrowed_book.book.bPrice
        user_model.save()

        messages.success(request, f'Book "{borrowed_book.book.title}" returned successfully.')

    return redirect('profile') 

def custom_logout(request):
    logout(request)
    return redirect('home')
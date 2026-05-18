from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# ---------------- HOME (FORM ADD) ----------------
def home(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')

    return render(request, 'home.html', {'form': form})


# ---------------- RESULT PAGE ----------------
def result(request):
    students = Student.objects.all()
    return render(request, 'result.html', {'students': students})


# ---------------- ADD STUDENT ----------------
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('result')

    return render(request, 'add.html')


# ---------------- UPDATE STUDENT ----------------
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.password = request.POST['password']
  

        student.save()
        return redirect('result')

    return render(request, 'update.html', {'student': student})
def delete(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('result')




# ---------------- STATIC PAGES ----------------
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def tablepage(request):
    return render(request, "tablepage.html")

def services(request):
    return render(request, "services.html")

def testing(request):
    return render(request, "testing.html")

def index(request):
    return render(request, "index.html")

def table(request):
    return render(request, "table.html")

def movies(request):
    return render(request, "movies.html")

def reviews(request):
    return render(request, "reviews.html")

def sports(request):
    return render(request, "sports.html")

def cart(request):
    return render(request, "cart.html")

def fashion(request):
    return render(request, "fashion.html")

def shop(request):
    return render(request, "shop.html")

def fashioncontact(request):
    return render(request, "fashioncontact.html")
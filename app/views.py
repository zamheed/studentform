import csv

from django.http import HttpResponse
from django.views.generic import CreateView, ListView

from .models import StudentForm


# write a class to create the form and save into database
class AddStudent(CreateView):
    # import model class and define the model
    model = StudentForm
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# write class to view the list
class StudentsDetails(ListView):
    model = StudentForm


# write a function to download csv
def csvDownload(request):
    # create a http response instance
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    # get data from model
    data = StudentForm.objects.all()
    # write the data to the csv file
    for rows in data:
        writer.writerow([rows.Name, rows.Age, rows.Gender])
    # return http response instance
    return response

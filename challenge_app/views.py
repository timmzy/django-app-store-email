from django.views.generic import TemplateView, ListView, FormView
from challenge_app.models import Detail
from challenge_app.forms import DetailForm

# Create your views here.

class HomeView(TemplateView):
    """
    Homepage
    """
    template_name = 'home.html'

class EmailList(ListView):
    """
    Email list
    """
    template_name = 'list.html'
    model = Detail
    context_object_name = "emails"


class AddEmail(FormView):
    """
    Page for adding email to database
    """
    template_name = 'add.html'
    success_url = "/list"
    form_class = DetailForm

    def form_valid(self, form):
        form.save()
        return super(AddEmail, self).form_valid(form)



from django.views import generic
from .forms import InquiryForm

# Create your views here.
def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="index.html"

class InquiryView(generic.FormView):
    template_name="diary/templates/inquiry.html"
    form_class=InquiryForm
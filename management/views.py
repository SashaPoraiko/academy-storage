from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from management.models import Feedback


# todo fix CSRF verification failed
@method_decorator(csrf_exempt, name='dispatch')
class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ('email', 'phone', 'name', 'message')

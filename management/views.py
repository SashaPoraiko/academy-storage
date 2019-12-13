from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from management.models import Feedback
from sky_storage.settings import HOST, EMAIL_HOST_USER


@method_decorator(csrf_exempt, name='dispatch')
class AjaxFeedbackCreateView(CreateView):
    model = Feedback
    success_url = '/'
    fields = ('email', 'phone', 'name', 'message')

    def form_invalid(self, form):
        super().form_invalid(form)
        return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        super().form_valid(form)
        # todo use send email
        self.send_email()
        return JsonResponse({
            'pk': self.object.pk,
        })

    def send_email(self):
        # todo write and use
        # send email using the self.cleaned_data dictionary
        form_kwargs = self.get_form_kwargs()["data"]

        context = {
            'host': HOST,
            'name': form_kwargs.get("name"),
            'email': form_kwargs.get("email"),
            'message': form_kwargs.get("message"),
            'phone': form_kwargs.get("phone"),
        }
        text_content = f'Feedback from: {form_kwargs.get("name")}, with email: {form_kwargs.get("email")},' \
                       f' his message is: {form_kwargs.get("message")},and his phone number are:' \
                       f' {form_kwargs.get("phone")}'

        html_content = render_to_string('emails/feedback.html', context)
        msg = EmailMultiAlternatives('Feedback', text_content, f'{form_kwargs.get("name")}', [EMAIL_HOST_USER])
        # msg.attach_alternative(html_content, "text/html")
        msg.send()

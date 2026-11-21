from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import SmsForm


@require_http_methods(["GET", "HEAD", "POST"])
def compose_sms(request):
    form = SmsForm()
    submitted = False
    if request.method == "POST":
        form = SmsForm(request.POST)
        submitted = form.is_valid()

    return render(
        request, "sms_app/compose.html", {"form": form, "submitted": submitted}
    )

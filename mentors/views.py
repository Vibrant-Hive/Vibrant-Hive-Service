from mentors.forms import UserForm


# Create your views here.
def create_account(request):
    # if request.POST:
    form = UserForm(json.loads(request.body.decode('utf-8')))
    if form.is_valid():
        save = form.save()
        return HttpResponse("Success")
    else:
        errors = form.errors
        print(errors)
        return HttpResponse("Failed")

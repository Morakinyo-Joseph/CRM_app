from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()

    context = {
        "leads": leads
    }
    return render(request, 'leads/leads_list.html', context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    print(f"Primary key/id = {pk}")

    context = {
        "lead": lead
    }

    print(lead.first_name)

    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    form = LeadModelForm()

    if request.method == 'POST':
        print('Receiving a post request')

        form = LeadModelForm(request.POST)

        if form.is_valid():
            print('Form is valid')
            print(form.cleaned_data)
            print(f"form is valid {form.is_valid}")
            form.save()

            print('New lead has being created')

            return redirect('/leads')

    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)


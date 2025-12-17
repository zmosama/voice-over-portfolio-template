from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import VoiceOver
from .forms import ContactForm

def home(request):
    featured_items = VoiceOver.objects.filter(is_featured=True).order_by('-created_at')[:3]
    return render(request, 'portfolio/home.html', {
        'featured_items': featured_items
    })

def portfolio_list(request):
    items = VoiceOver.objects.all().order_by('-created_at')
    return render(request, 'portfolio/portfolio_list.html', {
        'items': items
    })

def portfolio_detail(request, slug):
    item = get_object_or_404(VoiceOver, slug=slug)
    return render(request, 'portfolio/portfolio_detail.html', {
        'item': item
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real app, send email here
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {
        'form': form
    })

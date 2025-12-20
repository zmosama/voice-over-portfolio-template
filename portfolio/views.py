from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.urls import reverse
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
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {
        'form': form
    })

def search_api(request):
    """
    API endpoint for smart search
    Searches in: title, description, category
    """
    query = request.GET.get('q', '').strip()

    if not query:
        return JsonResponse({'results': []})

    # Search in title, description, and category
    results = VoiceOver.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(category__icontains=query)
    ).order_by('-created_at')[:10]  # Limit to 10 results

    # Format results for JSON response
    data = {
        'results': [
            {
                'title': item.title,
                'description': item.description[:150] + '...' if len(item.description) > 150 else item.description,
                'category': item.category,
                'category_display': item.get_category_display(),
                'url': f'/portfolio/{item.slug}/',
                'cover_image': item.cover_image.url if item.cover_image else None,
                'date': item.created_at.strftime('%b %Y')
            }
            for item in results
        ]
    }

    return JsonResponse(data)

def sitemap(request):
    """
    Generate XML sitemap for SEO
    """
    domain = 'https://basma.mosama.me'

    # Static pages
    urls = [
        {'loc': domain + '/', 'priority': '1.0', 'changefreq': 'weekly'},
        {'loc': domain + '/portfolio/', 'priority': '0.9', 'changefreq': 'daily'},
        {'loc': domain + '/contact/', 'priority': '0.7', 'changefreq': 'monthly'},
    ]

    # Dynamic portfolio items
    items = VoiceOver.objects.all()
    for item in items:
        urls.append({
            'loc': domain + f'/portfolio/{item.slug}/',
            'priority': '0.8',
            'changefreq': 'weekly',
            'lastmod': item.updated_at.strftime('%Y-%m-%d')
        })

    # Build XML
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url in urls:
        xml.append('  <url>')
        xml.append(f'    <loc>{url["loc"]}</loc>')
        if 'lastmod' in url:
            xml.append(f'    <lastmod>{url["lastmod"]}</lastmod>')
        xml.append(f'    <changefreq>{url["changefreq"]}</changefreq>')
        xml.append(f'    <priority>{url["priority"]}</priority>')
        xml.append('  </url>')

    xml.append('</urlset>')

    return HttpResponse('\n'.join(xml), content_type='application/xml')

def robots_txt(request):
    """
    Generate robots.txt for SEO
    """
    lines = [
        'User-agent: *',
        'Allow: /',
        'Disallow: /admin/',
        'Disallow: /api/',
        '',
        f'Sitemap: https://basma.mosama.me/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')

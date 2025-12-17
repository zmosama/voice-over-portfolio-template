from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500',
        'placeholder': 'your@email.com'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500',
        'placeholder': 'Project Inquiry'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500 h-32',
        'placeholder': 'Tell me about your project...',
        'rows': 4
    }))

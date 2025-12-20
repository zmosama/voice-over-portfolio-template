from django import forms

from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500',
                'placeholder': 'your@email.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500',
                'placeholder': 'Project Inquiry'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-navy-800 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-neon-pink focus:ring-1 focus:ring-neon-pink transition-all placeholder-gray-500 h-32',
                'placeholder': 'Tell me about your project...',
                'rows': 4
            })
        }

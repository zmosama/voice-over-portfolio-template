from django import template

register = template.Library()

@register.filter
def category_color(category):
    """Returns a neon color class for each category"""
    colors = {
        'ads': 'text-pink-400',
        'narration': 'text-cyan-400',
        'documentary': 'text-purple-400',
        'dubbing': 'text-yellow-400',
        'books': 'text-green-400',
        'radio': 'text-orange-400',
        'ivr': 'text-blue-400',
        'podcast': 'text-lime-400',
        'elearning': 'text-teal-400',
        'other': 'text-gray-400',
    }
    return colors.get(category, 'text-neon-blue')

@register.filter
def category_bg(category):
    """Returns a neon background color class for each category"""
    colors = {
        'ads': 'bg-pink-500/10 border-pink-500/30',
        'narration': 'bg-cyan-500/10 border-cyan-500/30',
        'documentary': 'bg-purple-500/10 border-purple-500/30',
        'dubbing': 'bg-yellow-500/10 border-yellow-500/30',
        'books': 'bg-green-500/10 border-green-500/30',
        'radio': 'bg-orange-500/10 border-orange-500/30',
        'ivr': 'bg-blue-500/10 border-blue-500/30',
        'podcast': 'bg-lime-500/10 border-lime-500/30',
        'elearning': 'bg-teal-500/10 border-teal-500/30',
        'other': 'bg-gray-500/10 border-gray-500/30',
    }
    return colors.get(category, 'bg-neon-blue/10 border-neon-blue/30')

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .chat_utils import generate_response

# Nous utiliserons la session pour conserver l'historique de conversation
@csrf_exempt
def chat_view(request):
    if 'history' not in request.session:
        # Initialise l'historique vide
        request.session['history'] = []
    
    history = request.session.get('history', [])
    
    response_text = None
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        if user_input:
            response_text = generate_response(history, user_input)
            # Sauvegarder l'historique dans la session
            request.session['history'] = history
    
    context = {
        'history': history,
        'response': response_text
    }
    return render(request, "chat/chat.html", context)

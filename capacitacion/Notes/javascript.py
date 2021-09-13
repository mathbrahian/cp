import json

from django.http import HttpResponse
from django.urls import reverse


def var_javascript(request):
    """Almacena las variables javascript para el contexto global del app

    Args:
        request : petición del usuario

    Returns:
        Diccionario con todas las claves del contexto en js.
    """
    context = {}
    # api de notes
    context["api_notes_list"] = reverse(
        "Notes:notas-list"
    )
    let = "let Django = " + json.dumps(context, indent=1)
    return HttpResponse(let, content_type="application/javascript")

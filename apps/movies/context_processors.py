from apps.movies.models import Contacts

def global_contacts(request):
    return {
        'contacts': Contacts.objects.first()
    }
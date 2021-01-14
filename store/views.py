from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from .models import Album, Artist, Contact, Booking
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm, ParagraphErrorList
from django.db import transaction, IntegrityError
# Create your views here.

def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:6]
    context = {
        'albums':albums,
    }
    return render(request, 'store/index.html', context)    

def listing(request):
    albums_list = Album.objects.all()
    paginator = Paginator(albums_list, 3)
    page_number = request.GET.get('page')
    try:
        albums = paginator.page(page_number)
    except InvalidPage:
        albums = paginator.page(1)
    context = {
        'paginate':True,
        'albums':albums
    }
    return render(request, 'store/listing.html', context)

@transaction.atomic
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists_name = " ".join([artist.name for artist in album.artists.all()])
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class = ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        contact = Contact.objects.create(
                            email=email,
                            name=name
                        )
                    else:
                        contact = contact.first()

                    album = get_object_or_404(Album, id=album_id)
                    booking = Booking.objects.create(
                        contact=contact,
                        album=album
                    )
                    album.available = False
                    album.save()
                    context = {
                        'album_title': album.title
                    }
                    return render(request, 'store/merci.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = ContactForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requete %s"%query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)
    
from django.test import TestCase
from django.urls import reverse

from .models import Album, Artist, Booking, Contact

class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

# class DetailPageTestCase(TestCase):

#     def test_detail_page_returns_200(self):
#         impossible = Album.objects.create(title="Transmission Impossible")
#         album_id = Album.objects.get(title='Transmission Impossible').id
#         response = self.client.get(reverse('store:detail', args=(album_id,)))
#         self.assertEqual(response.status_code, 200)

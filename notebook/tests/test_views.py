from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.test import TestCase

from ..models import TextNote
from ..views import Homepage

class HomePageTest(TestCase):
    '''
    Tests that the home page returns a list of notes
    '''
    def setUp(self):
        TextNote.objects.create(
            content='first',
            is_published=False,
        )
        TextNote.objects.create(
            content='second',
            is_published=True,
        )
        TextNote.objects.create(
            content='third',
            is_published=True,
        )

    def test_homepage_view(self):
        '''
        visit homepg, get list of notes that are published
        test homepageview returns correct context objects
        '''
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['latest_published_textnotes'],
            ['<TextNote: second>', '<TextNote: third>']
        )

import datetime
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from notebook.views import homepage
from notebook.models import TextNote

#things to test> create>save>integrity>query&filter>viewreturns proper context>templaterenders proper html

class NoteModelTest(TestCase):
    '''
    Tests the model layer. Check we can create, save, query, and filter
    objects as well as the integrity of said objects.  
    '''
    def setUp(self):
        '''
        create TextNotes objects through both instantiation of 
        the model + save(), as well as using the create() method
        shortcut
        '''
        #here we use instantiation + save()
        mynote = TextNote()
        mynote.content = b'<html>hello world</html>'
        mynote.is_published = False
        mynote.save()

        #here we use the create() shortcut
        TextNote.objects.create(
            content='first one where pub is true',
            is_published=True,
        )
        TextNote.objects.create(
            content='hello',
            is_published=False,
        )
        TextNote.objects.create(
            content='world',
            is_published=True,
        )
        TextNote.objects.create(
            content='foo',
            is_published=True,
        )

    def test_integrity_and_querying_of_textnotes(self):
        '''
        Test TextNote objects were saved properly
        '''

        all_notes = TextNote.objects.all()
        # check that we have 5 items
        self.assertEqual(all_notes.count(), 5)
    
        #query notes were published=True, there should be 3
        published_notes = all_notes.filter(is_published=True)
        self.assertEqual(published_notes.count(), 3)
        
        #out of the published notes, get the first one, check its attributes
        ##FIX THIS!!!! DON'T ASSUME DJANGO ORDERS THINGS CHRONOLOGICALLY
        #published_notes.order_by('create_date')
        ##also double check my assertions arn't backwards
        first_note = published_notes.first()
        self.assertIn('first', first_note.content)
        self.assertTrue(first_note.is_published)

class HomePageTest(TestCase):
    '''
    Tests that the home page returns a list of notes
    '''
    def setUp(self):
        TextNote.objects.create(
            content='hello',
            is_published=False,
        )
        TextNote.objects.create(
            content='world',
            is_published=True,
        )
        TextNote.objects.create(
            content='foo',
            is_published=True,
        )

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_view(self):
        '''
        visit homepg, get list of notes that are published
        test homepageview returns correct context objects
        '''

        request = HttpRequest()
        response = homepage(request)



       #self.assertTrue(response.content.startswith(b'<html>'))
       #self.assertIn(b'<title>mac</title>', response.content)
       #self.assertTrue(response.content.endswith(b'</html>'))




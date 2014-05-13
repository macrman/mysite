from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from notebook.views import homepage
from notebook.models import TextNote


class NoteModelTest(TestCase):
    '''
    Tests the model layer. Check we can create, save, query, and filter
    objects as well as the integrity of said objects.  
    '''
    def setUp(self):
        '''
        create TextNotes objects, publish 2,4,5
        '''
        #here we use instantiation + save()
        mynote = TextNote()
        mynote.content = '1st'
        mynote.is_published = False
        mynote.save()

        #here we use the create() shortcut
        TextNote.objects.create(
            content='2nd',
            is_published=True,
        )
        TextNote.objects.create(
            content='3rd',
            is_published=False,
        )
        TextNote.objects.create(
            content='4th',
            is_published=True,
        )
        TextNote.objects.create(
            content='5th',
            is_published=True,
        )

    def test_integrity(self):
        '''
        Test TextNote objects were saved properly
        '''

        all_notes = TextNote.objects.all()
        # check that we have 5 items
        self.assertEqual(all_notes.count(), 5)

    def test_filtering_and_querying(self):
    
        #let's get all the published notes, there should be 3
        published_notes = TextNote.objects.filter(is_published=True)
        self.assertEqual(published_notes.count(), 3)

        #sort the notes by pub_date
        sorted_pub_notes = published_notes.order_by('pub_date')

        #get the first one, first note should be the first one 'published'
        # aka #2
        first_pubed_note = sorted_pub_notes.first()
        self.assertEqual(first_pubed_note.content, '2nd')

    def test_publishing_notes(self):
        '''
        When a user publishes a note, the pub_date should
        automatically be added.
        '''
        # lets get one of the unpublished notes, sort by date created
        unpubed_notes = TextNote.objects.filter(is_published=False).order_by('date_created')

        # we'll take the newest one and publish it (should be #3)
        to_be_pubed = unpubed_notes.last()
        to_be_pubed.is_published = True
        to_be_pubed.save()


        self.assertEqual(to_be_pubed.content, '3rd') 

        # now lets query all the pubed notes and check the one
        # we just pubed is the newest
        pubed_notes = TextNote.objects.filter(is_published=True)
        latest_note = pubed_notes.order_by('pub_date').last()
        self.assertEqual(latest_note.content, '3rd')

        
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




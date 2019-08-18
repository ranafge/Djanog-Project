from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import home
from .models import Board
from .views import board_topics, new_topic

class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board desc')

    def test_board_topics_view_seccess_status_code(self):
        url = reverse('board_topics', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)






class HomeTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django description')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs = {'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs = {'pk':10})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_view_status(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board description')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)


































from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="First Todo", body="a body Here")
    
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'First Todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_body = f'{todo.body}'
        self.assertEquals(expected_object_body, 'a body Here')
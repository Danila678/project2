from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Course, Module, Material, Enrollment, UserProgress

class CourseTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        data = {
            'title': 'Test Course',
            'description': 'Test Description',
            'start_date': '2024-07-01T00:00:00Z',
            'end_date': '2024-12-31T00:00:00Z',
            'instructor': self.user.id
        }
        response = self.client.post('/courses/', data)
        self.assertEqual(response.status_code, 201)

    def test_get_courses(self):
        Course.objects.create(
            title='Test Course 1',
            description='Test Description 1',
            start_date='2024-07-01T00:00:00Z',
            end_date='2024-12-31T00:00:00Z',
            instructor=self.user
        )
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_course(self):
        course = Course.objects.create(
            title='Test Course 1',
            description='Test Description 1',
            start_date='2024-07-01T00:00:00Z',
            end_date='2024-12-31T00:00:00Z',
            instructor=self.user
        )
        data = {
            'title': 'Updated Test Course',
            'description': 'Updated Test Description',
            'start_date': '2024-08-01T00:00:00Z',
            'end_date': '2025-01-01T00:00:00Z',
            'instructor': self.user.id
        }
        response = self.client.put(f'/courses/{course.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Test Course')

    def test_delete_course(self):
        course = Course.objects.create(
            title='Test Course 1',
            description='Test Description 1',
            start_date='2024-07-01T00:00:00Z',
            end_date='2024-12-31T00:00:00Z',
            instructor=self.user
        )
        response = self.client.delete(f'/courses/{course.id}/')
        self.assertEqual(response.status_code, 204)

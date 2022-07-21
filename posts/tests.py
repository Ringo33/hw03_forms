from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

User = get_user_model()


class ProfileTest(TestCase):

    def setUp(self):
        # создание тестового клиента — подходящая задача для функции setUp()
        self.client = Client()
        self.nonauth_client = Client()
        # создаём пользователя
        self.user = User.objects.create_user(
            username="test_user_1",
            email="test_1@ya.ru",
            password="test_123"
        )
        # создаём пост от имени пользователя
        self.post = Post.objects.create(text="Test post from test_user_1", author=self.user)


    def test_new_user_profile(self):

        response = self.client.get(reverse('profile', kwargs={'username': self.user.username}))
        print(reverse('profile', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)


    def test_auth_user_new_post(self):

        self.client.login(username="test_user_1", password="test_123")
        print(self.client.login(username="test_user_1", password="test_123"))
        self.client.post(reverse('new_post'), data={'text': 'New post from test_user_1'})
        response = self.client.get(reverse('post', kwargs={'username': self.user.username, 'post_id': 2}))
        print(response.context['post'])
        self.assertEqual(str(response.context['post']), 'New post from test_user_1')


    def test_not_auth_user_no_new_post(self):

        response = self.nonauth_client.get("/new/", follow=True)
        self.assertRedirects(response, "/auth/login/?next=/new/", status_code=302, target_status_code=200)


    def test_new_post_on_index_profile_post(self):

        self.client.login(username="test_user_1", password="test_123")
        for url in (
                '',
                '/test_user_1/',
                reverse('post', kwargs={'username': self.user.username,
                                        'post_id': self.post.id})
        ):
            self.assertContains(self.client.get(url), "Test post from test_user_1")

    def test_auth_user_edit_post(self):

        self.client.login(username="test_user_1", password="test_123")
        self.client.post(
            reverse('post_edit',
                    kwargs={'username': self.user.username,
                            'post_id': self.post.id}
                    ),
            data={'text': 'New post from test_user_1'}
        )
        for url in (
                '',
                '/test_user_1/',
                reverse('post', kwargs={'username': self.user.username,
                                        'post_id': self.post.id})
        ):
            self.assertContains(self.client.get(url), "New post from test_user_1")


    def test_status_404(self):
        response = self.client.get("/qwerty123123/")
        self.assertEqual(response.status_code, 404)
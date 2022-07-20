from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

User = get_user_model()


class ProfileTest(TestCase):
    def setUp(self):
        # создание тестового клиента — подходящая задача для функции setUp()
        self.client = Client()
        # создаём пользователя
        self.user = User.objects.create_user(
            username="test_user1",
            email="test1@ya.ru",
            password="test_1233211"
        )
        # создаём пост от имени пользователя
        self.post = Post.objects.create(text="Test post", author=self.user)

    def test_profile(self):
        # формируем GET-запрос к странице сайта
        # response = self.client.get("/sarah/")
        response = self.client.get(reverse('profile', kwargs={'username': self.post.author}))
        print(reverse('profile', kwargs={'username': self.post.author}))
        # # проверяем что страница найдена
        self.assertEqual(response.status_code, 200)
        #
        # # проверяем, что при отрисовке страницы был получен список из 1 записи
        # self.assertEqual(response.context["posts_count"], 2)

        # # проверяем, что объект пользователя, переданный в шаблон,
        # # соответствует пользователю, которого мы создали
        # self.assertIsInstance(response.context["profile"], User)
        # self.assertEqual(response.context["profile"].username, self.user.username)

    def test_new_user_profile(self):
        self.user = User.objects.create_user(
            username="user2", email="123@bk.ru", password="12345"
        )
        response = self.client.get("/user2/")
        self.assertEqual(response.status_code, 200)

    def test_auth_user_new_post(self):
        self.client.login(username="test_user1", password="test_1233211")
        print(self.client.login(username="test_user1", password="test_1233211"))
        self.post = Post.objects.create(text="Test of creation of new post", author=self.user)
        response = self.client.get(reverse('post', kwargs={'username': self.post.author, 'post_id': self.post.id}))
        print(reverse('post', kwargs={'username': self.post.author, 'post_id': self.post.id}))
        self.assertEqual(response.status_code, 200)
        print(self.client.get(reverse('post', kwargs={'username': self.post.author, 'post_id': self.post.id})).content)

    def test_not_auth_user_no_new_post(self):
        response = self.client.get("/new/", follow=True)
        print(response.redirect_chain)

    def test_new_post_on_index_profile_post(self):
        print(self.client.login(username='user2', password='12345'))
        new_post = 'Yahoo'
        # self.post = Post.objects.create(text=new_post, author=User.objects.get(username='user2'))
        response = self.client.get('')

        self.assertContains(response, 'Yahoo')
        # self.assertIn('Yahoo', str(response.content))
        # print(response.content)

    def test_auth_user_edit_post(self):
        self.client.login(username='user2', password='12345')
        print(self.client.login(username='user2', password='12345'))
        new_text = 'Hello gay12345!'

        # self.post = Post.objects.get(id=126)
        # self.post.text = new_text
        # self.post.save()
        # self.assertEqual(self.post.text, new_text)
        # response = self.client.get("/user2/126/")
        # self.assertEqual(str(response.context['post']), new_text)

        # response = self.client.get("/user2/126")
        # self.assertContains(response, new_text)
        # print(response)

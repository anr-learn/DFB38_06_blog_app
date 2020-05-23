# blog05_app/tests.py

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import BlogPost


class BlogTests(TestCase):
	""" """

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username="testuser",
			email="testuser@myemail.com",
			password="secret")

		self.post = BlogPost.objects.create(
			postTitle="My Blog Title",
			postBody="This is the blog body",
			postAuthor=self.user)

	def test_string_form(self):
		""" """
		title = "My Sample Title"
		expStg = f"BlogPost[{title}]"
		post = BlogPost(postTitle=title)
		self.assertEqual(str(post), expStg)

	def test_post_content(self):
		""" """
		self.assertEqual(f"{self.post.postTitle}", "My Blog Title")
		self.assertEqual(f"{self.post.postBody}", "This is the blog body")
		self.assertEqual(f"{self.post.postAuthor}", "testuser")

	def test_post_list_view(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "This is the blog body")
		self.assertTemplateUsed(response, "home.html")

	def test_good_post_detail_view(self):
		""" 'good' detail view """
		response = self.client.get("/post/1/")
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "This is the blog body")
		self.assertTemplateUsed(response, "post_detail.html")
		#print(f"@@@ @@@ {dir(response)}")
		#print(f"@@@ @@@ template name: {response.template_name}")

	def test_nosuch_detail(self):
		""" try fetching a non-existent BlogPost obj """
		response = self.client.get("/post/2/")
		self.assertEqual(response.status_code, 404)
		# We got an error before trying to use a template,
		# so no template was accessed
		###print(f"@@@ {response}")
		###print(f"@@@ @@@ template name: {response.template_name}")
		###self.assertTemplateUsed(response, None)
		self.assertFalse(hasattr(response, "template_name"))


### end ###

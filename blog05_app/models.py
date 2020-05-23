# DFB38_06_blog_app/blog05_app/models.py

from django.db import models


class BlogPost(models.Model):
	""" A post to the blog """

	# NOTE Django adds a primary key field 'id' that contains
	# an auto-incrementing int value, starting at 1.
	# Ref'd as 'id' or 'pk'

	postTitle = models.CharField(max_length=200)
	# many-to-one (many posts per each author)
	# (Each post has only 1 author)
	postAuthor = models.ForeignKey(
					"auth.User",
					on_delete=models.CASCADE)
	postBody = models.TextField()

	def __str__(self):
		return ("%s[%s]" % 
			(self.__class__.__name__,
			 self.postTitle))


### end ###

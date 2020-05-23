# DFB38_05_blog_app/blog05_app/views.py

#from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogListView(ListView):
	""" """

	model = BlogPost

	template_name = "home.html"

	# Replace 'object_list' in home page with this more descriptive name
	context_object_name = "all_block_post_objects"


class BlogDetailView(DetailView):
	""" A DetailView expects a primary key -- to obtain the
	details object.
	Can provide either a primary key (aka PK) or a 'slug'.	
	"""

	model = BlogPost

	template_name = "post_detail.html"

	# In the template, you can use either 'object' or 
	# 'blogpost' (lower-cased class name)
	# to access the view.
	# If you provide context_object_name explicitly,
	# you use that instead of 'object'.
	context_object_name = "blog_post_detail_object"




### end ###

from django.conf.urls import patterns, include, url
from idmpirate import views
from idmpirate.views import Blog  # importing Blog controller class
from idmpirate.views import Sign_in
from django.contrib import admin

admin.autodiscover()

blog = Blog()  # Blog controller
sign_in = Sign_in()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'simple_blog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^address/', include(admin.site.urls),name="address"),
                       url(r'^addblog/', blog.createBlog, name="create"),
                       url(r'^login/', sign_in.sign_in, name="sign_in"),
                       url(r'^', views.index),

                       )

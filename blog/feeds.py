from django.contrib.syndication.views import Feed

from .models import Post

class AllpostRssFeed(Feed):
    title = 'Django 我的博客'
    link = '/'
    description = 'django 测试'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s ' % (item.category,item.title)

    def item_description(self, item):
        return item.body
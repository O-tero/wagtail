from django.urls import path

from wagtail.admin.views.pages.listing import IndexView

from .base import ViewSet


class PageListingViewSet(ViewSet):
    #: The view class to use for the index view; must be a subclass of ``wagtail.admin.views.pages.listing.IndexView``.
    index_view_class = IndexView

    def get_index_view_kwargs(self, **kwargs):
        return {
            "index_url_name": self.get_url_name("index"),
            "index_results_url_name": self.get_url_name("index_results"),
            **kwargs,
        }

    @property
    def index_view(self):
        return self.construct_view(
            self.index_view_class, **self.get_index_view_kwargs()
        )

    @property
    def index_results_view(self):
        return self.construct_view(
            self.index_view_class, **self.get_index_view_kwargs(), results_only=True
        )

    def get_urlpatterns(self):
        return [
            path("", self.index_view, name="index"),
            path("results/", self.index_results_view, name="index_results"),
        ]

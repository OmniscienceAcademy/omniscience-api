"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "get-direct-results/<str:user_query>/<int:min_year>/<int:max_year>/",
        views.get_directs_results,
    ),
    path("search/<str:user_query>/", views.search_title),
    path("searchabstract/<str:string>/", views.search_abstract),
    path("get-article-by-id/<int:paper_id>/", views.get_article_by_id),
    # path("get-article-by-id/<int:paper_id>/", views.get_article_by_id),
    path("get-articles-by-id/", views.get_articles_by_id),
    path(
        # potentially multiple swipe_session_token by session_id
        "get-results-swipe/<str:swipe_session_token>/",
        views.get_results_swipe,
        name="get-results-swipe",
    ),
    path("top-articles/", views.top_articles),
    # path at the root of the application
    path("", views.index),
    path("run_tests/", views.run_tests),
    path("get_fields_of_study_level_0/", views.get_fields_of_study_level_0_info),
    path("get_fields_of_study_by_ids/", views.get_fields_of_study_by_ids),
    path(
        "get_field_of_study_children/<int:field_of_study_id>/",
        views.get_children_of_field_of_study_id,
    ),
    path("search_fields_of_study/<str:query>/", views.search_fields_of_study),
    path(
        "get_authors_of_field_of_study/<int:field_of_study_id>/<int:only_french>/",
        views.get_authors_of_field_of_study,
    ),
    path(
        "get_top_github_by_field_of_study/<int:field_of_study_id>/",
        views.get_top_github_by_field_of_study,
    ),
    path("get_search_authors/<str:query>/", views.get_search_authors),
    path(
        "get_main_papers_of_field_of_study/<int:field_of_study_id>/",
        views.get_main_papers_of_field_of_study,
    ),
    # get_resources_field_of_study
    path(
        "get_resources_field_of_study/<int:field_of_study_id>/",
        views.get_resources_field_of_study,
    ),
    path("get-authors-by-ids/", views.get_authors_by_ids),
    path("get-author-by-id/<int:author_id>/", views.get_author_by_id),
    path("get-autocompletion/<str:user_query>/", views.get_autocompletion),
]

from django.conf import settings
from django.views import static
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from elasticsearch_dsl import TermsFacet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    CompoundSearchFilterBackend,
    DefaultOrderingFilterBackend,
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_TERMS,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)


from .documents import DocumentDoc
from .backends import (
    NestedFacetedSearchFilterBackend,
    DefaultAwareNestedFilteringFilterBackend,
    LOOKUP_QUERY_MATCH_PHRASE,
)
from .serializers import (
    InfoLevelSerializer,
    CountrySerializer,
    DataSetSerializer,
    DataTypeSerializer,
    ResourceTypeSerializer,
    TopicCategorySerializer,
    DocumentDocSerializer,
    NUTSLevelSerializer,
    KeywordSerializer,
    LanguageSerializer,
    DocSerializer,
)

from .models import (
    DInfoLevel,
    DCountry,
    DDataType,
    DDataSet,
    DResourceType,
    DTopicCategory,
    DNutsLevel,
    DKeyword,
    DLanguage,
    Document,
)


# Facets viewsets


class InfoLevelViewSet(ReadOnlyModelViewSet):
    queryset = DInfoLevel.objects.all()
    serializer_class = InfoLevelSerializer
    pagination_class = None


class CountryViewSet(ReadOnlyModelViewSet):
    queryset = DCountry.objects.all()
    serializer_class = CountrySerializer
    pagination_class = None


class DataTypeViewSet(ReadOnlyModelViewSet):
    queryset = DDataType.objects.all()
    serializer_class = DataTypeSerializer
    pagination_class = None


class DataSetViewSet(ReadOnlyModelViewSet):
    queryset = DDataSet.objects.all()
    serializer_class = DataSetSerializer
    pagination_class = None


class ResourceTypeViewSet(ReadOnlyModelViewSet):
    queryset = DResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    pagination_class = None


class TopicCategoryViewSet(ReadOnlyModelViewSet):
    queryset = DTopicCategory.objects.all()
    serializer_class = TopicCategorySerializer
    pagination_class = None


class NUTSLevelViewSet(ReadOnlyModelViewSet):
    queryset = DNutsLevel.objects.all()
    serializer_class = NUTSLevelSerializer
    pagination_class = None


class KeywordViewSet(ReadOnlyModelViewSet):
    queryset = DKeyword.objects.all()
    serializer_class = KeywordSerializer
    pagination_class = None


class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = DLanguage.objects.all()
    serializer_class = LanguageSerializer
    pagination_class = None


class SearchPageNumberPagination(PageNumberPagination):
    """
    Pagination class for the search viewset. Accepts custom page sizes in
    URL params, and trims the verbose facets structure returned by
    `django_elasticsearch_dsl_drf.PageNumberPagination.get_facets`.
    """

    page_size_query_param = "page_size"

    def get_facets(self, page=None):
        raw_facets = super().get_facets(page)
        if raw_facets is not None:
            facets = {}
            for filter_key, data in raw_facets.items():
                field = filter_key[8:]  # remove '_filter_' prefix
                if filter_key in data[filter_key]:
                    _data = {
                        b["key"]: b["doc_count"]
                        for b in data[filter_key][filter_key][field]["buckets"]
                    }
                else:
                    _data = {
                        b["key"]: b["doc_count"]
                        for b in data[filter_key][field]["buckets"]
                    }
                facets[field] = _data
            return facets


class SearchViewSet(BaseDocumentViewSet):
    document = DocumentDoc
    serializer_class = DocumentDocSerializer
    pagination_class = SearchPageNumberPagination
    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        DefaultAwareNestedFilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
        DefaultOrderingFilterBackend,
        NestedFacetedSearchFilterBackend,
    ]
    search_fields = ("title", "description")

    # Facets for DocumentDoc's non-nested fields
    facets = (
        "data_type",
        "data_set",
        "data_source",
        "info_level",
        "topic_category",
        "resource_type",
        "published_year",
        "data_collection_start_year",
        "data_collection_end_year",
        "next_update_year",
    )

    filter_fields = {
        f: {
            "field": f,
            "lookups": [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
                LOOKUP_QUERY_MATCH_PHRASE,
            ],
        }
        for f in facets
    }

    nested_filter_fields = {
        "country": {"field": "countries.name", "path": "countries"},
        "keyword": {
            "field": "keywords.name",
            "path": "keywords",
            "default_lookup": LOOKUP_QUERY_MATCH_PHRASE,
            "lookups": [LOOKUP_QUERY_MATCH_PHRASE],
            "disjunction": settings.KEYWORDS_DISJUNCTION,
        },
        "nuts_level": {"field": "nuts_levels.name", "path": "nuts_levels"},
    }

    faceted_search_fields = {
        field: {
            "field": field,
            "enabled": True,
            "global": True,
            "options": {
                # Dirty hack to force all facet values to show up in results
                # (setting size=0 does NOT work with aggregations).
                "size": 1000
            },
        }
        for field in facets
    }

    nested_faceted_search_fields = {
        "country": {
            "field": "countries.name",
            "path": "countries",
            "enabled": True,
            "facet": TermsFacet,
            "global": True,
            "options": {"size": 1000},
            "filter_field": "country",
        },
        "nuts_level": {
            "field": "nuts_levels.name",
            "path": "nuts_levels",
            "enabled": True,
            "facet": TermsFacet,
            "global": True,
            "options": {"size": 1000},
            "filter_field": "nuts_level",
        },
    }

    ordering_fields = {f: f for f in facets + ("country",)}
    ordering = ("_score",)


class DocumentViewSet(ReadOnlyModelViewSet):
    serializer_class = DocSerializer

    def get_queryset(self):
        return Document.objects.order_by("id").all()

    # @detail_route(methods=["get", "head"], renderer_classes=(StaticHTMLRenderer,))
    @action(methods=["get", "head"], renderer_classes=(StaticHTMLRenderer,), detail=True)
    def download(self, request, pk):
        doc_file = self.get_object().file
        if doc_file is None:
            Response(status=status.HTTP_404_NOT_FOUND)

        file = doc_file.file
        relpath = file.name

        if relpath is None or relpath == "":
            return Response(status=status.HTTP_404_NOT_FOUND)

        if settings.DEBUG:
            response = static.serve(
                request, path=relpath, document_root=file.storage.location
            )
        else:
            # this does "X-Sendfile" on nginx, see
            # https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/
            response = Response(
                headers={"X-Accel-Redirect": file.storage.path(relpath)}
            )

        response["Content-Disposition"] = f"attachment; filename={doc_file.name}"
        return response


class CollectionYearsRangeViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        earliest, latest = Document.collection_range()
        return Response({"min": earliest, "max": latest})


class PublicationYearsViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        return Response(list(Document.publication_years()))

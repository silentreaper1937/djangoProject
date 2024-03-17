from rest_framework.versioning import QueryParameterVersioning


class MyVersion(QueryParameterVersioning):

    def determine_version(self, request, *args, **kwargs):
        version = request.query_params.get('version')
        if not version:
            version = 'v1'
        return version
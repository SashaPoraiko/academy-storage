def parse_query_params(params, fields=None):
    if fields is None:
        fields = ()
    for field_param, field_underscore in fields:
        if params.get(field_param):
            params[field_underscore] = params.get(field_param)
    return params

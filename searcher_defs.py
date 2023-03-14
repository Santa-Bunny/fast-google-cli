import config


def list_split(lists):
    simple_list = []
    for list in lists:
        for item in list:
            simple_list.append(item)
    return simple_list

def create_query(arg):
    query = list_split(arg)
    return ' '.join(query)

def create_site_list(sites_list):
    filter = ''
    for index, website in enumerate(sites_list):
            filter +='site:' + website
            if index == len(sites_list) - 1:
                filter += ')'
            else:
                filter += ' OR '
    return filter

def create_site_filter(arg):
    filter = '('
    if arg == None:
        filter += create_site_list(config.SITES_TO_SEARCH)
    else:
        filter += create_site_list(list_split(arg))
    return filter

def create_url(args):
    if args.all:
        return config.URL + create_query(args.query)
    return config.URL + create_query(args.query) + create_site_filter(args.custom)
# TODO figure out settings format
# probably split endpoints into a separate file
# or something maybe?


ENDPOINTS = {
    '/': {
        'service': 'papi.services.static.StaticData',
        'description': 'Personal Information',
        'data': {
            'name': 'Tosh',
            'email': 'toshism@gmail.com'
        }
    },
    '/code': {
        'service': 'papi.services.github.GitHub',
        'description': 'Github Activity Summary',
        'data': {
            'username': 'toshism',
            'data_type': 'summary'
        }
    },
    '/code/repos': {
        'service': 'papi.services.github.GitHub',
        'description': 'Github Repos',
        'data': {
            'username': 'toshism',
            'data_type': 'repos'
        }
    }

}

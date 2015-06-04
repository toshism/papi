# TODO figure out settings format
# probably split endpoints into a separate file
# or something maybe?

ENDPOINTS = {
    '/': {
        'service': 'services.static.static.StaticData',
        'data': {
            'name': 'Tosh',
            'email': 'toshism@gmail.com'
        }
    },
    'test': {
        'service': 'services.test',
        'data': {
            'name': 'Tosh',
            'email': 'toshism@gmail.com'
        }
    }
}

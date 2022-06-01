{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': [
        'base_setup',
        'sales_team',
        'mail',
        'calendar',
        'resource',
        'fetchmail',
        'utm',
        'web_tour',
        'contacts',
        'digest',
        'phone_validation',
    ],
    'application': True,
    'data': [
        'security/ir.model.access.csv'
    ]
}

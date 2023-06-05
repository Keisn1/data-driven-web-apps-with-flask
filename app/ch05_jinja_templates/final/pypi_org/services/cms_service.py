fake_db = {
    'company/history': {
        'page_title': 'Company history',
        'page_details': 'Details about company history...',
    },
    'company/employes': {
        'page_title': 'Our Team',
        'page_details': 'Details about company employees...',
    }
}

def get_page(url: str) -> dict:
    if not url:
        return {}

    url = url.strip().lower()
    page = fake_db.get(url, {})
    return page

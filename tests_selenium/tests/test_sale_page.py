def test_sale_header(sale_page):
    sale_page.open()
    sale_page.check_header_is_('Sale')

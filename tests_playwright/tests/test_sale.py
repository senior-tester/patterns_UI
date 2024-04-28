def test_sale_title(sale_page):
    sale_page.open()
    sale_page.check_title_is_('Sale')

#utf-8

"""
c.translate(str.maketrans(a, b)) ：这个会将c字符串中的字符根据a到b到映射做 翻译
"""
def test_tranlate():
    new_str = 'welcome to Mars'.translate(str.maketrans('wto', '123'))
    assert new_str == '1elc3me 23 Mars'

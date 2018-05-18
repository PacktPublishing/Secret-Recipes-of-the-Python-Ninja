>>> bag() == set()
True
>>> bag('a') == set('a')
True
>>> bag('ab') == set('a')
False
>>> bag('a') == set('ab')
False
>>> bag('aa') == set('a')
False
>>> bag('aa') == set('ab')
False
>>> bag('ac') == set('ab')
False
>>> bag('ac') <= set('ab')
False
>>> bag('ac') >= set('ab')
False
>>> bag('a') <= bag('a') < bag('aa')
True
>>> bag('aa') <= bag('a')
False

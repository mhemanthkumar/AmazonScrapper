from time import sleep
from AMZ_navigator import burl, conn, pages, purl
from AMZ_extract import fprod_asin, fprod_title, fprod_price, fprod_imgUrl, fprod_url

url_list = []
AMA_final_prod_list = []

search_query = 'lenovo ideapad'

burl, burl_list = burl(search_query)
resp_status, response = conn(burl)
print burl

c_page, t_page, items_list = pages(response)

print c_page, ':', t_page
print len(items_list)
print type(c_page)
print type(t_page)
for cp in range(int(c_page), t_page + 1):
    url_list = purl(cp, t_page, search_query, burl)

print url_list

for urlx in url_list:
    c_page, t_page, items_list = pages(response)
    for items in items_list:
        prod_ASIN = fprod_asin(items)
        #print prod_ASIN
        prod_Title = fprod_title(items)
#        print prod_Title
        prod_Price = fprod_price(items)
#        print prod_Price
        prod_ImgUrl = fprod_imgUrl(items)
        #print prod_ImgUrl
        prod_Url = fprod_url(items)
        #print prod_Url
        final_prod = {'Title': prod_Title,'Price': prod_Price, 'Image_url': prod_ImgUrl, 'prod_Url':prod_Url}
        AMA_final_prod_list.append(final_prod)
    sleep(5)

print len(AMA_final_prod_list)
for prod in AMA_final_prod_list:
    print prod['Title']
    print prod['Price']
    print prod['prod_Url']

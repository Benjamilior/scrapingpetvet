import requests

url = "https://petcity.cl/wp-admin/admin-ajax.php"

# Cambia '45844' por el ID del nuevo producto que deseas agregar al carrito
exmaples = "45844", "50956"

new_product_id = "50956"
payload = f"quantity=1&action=woodmart_ajax_add_to_cart&add-to-cart={new_product_id}"
headers = {
    "cookie": "woocommerce_items_in_cart=1; woocommerce_cart_hash=7a0e661746ab45f559692fbc13bb8744; wp_woocommerce_session_6f561ba7624d011ed2c30531bbb7fa44=t_af1b23ce69be146fecec3605cb8986%257C%257C1722623577%257C%257C1722619977%257C%257Cf178b156933e4b457268f302cefe6920",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,es-CL;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://petcity.cl",
    "Alt-Used": "petcity.cl",
    "Connection": "keep-alive",
    "Referer": "https://petcity.cl/tienda/bravecto-20-40kg/",
    "Cookie": "sib_cuid=2a461287-7b63-4c44-ad8d-634990a27725; _ga_PNJ5G476YR=GS1.1.1722450662.4.1.1722450708.0.0.0; _ga=GA1.1.564679806.1721675085; _gcl_au=1.1.93791507.1721675085; po_visitor=yQ7b8QSpZXa9; _fbp=fb.1.1721675086377.17395658860478704; PHPSESSID=2dec7f72a7afb44e425e0f8aa3b514e5; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-31%2016%3A18%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcity.cl%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2024-07-31%2015%3A08%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fpetcity.cl%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A128.0%29%20Gecko%2F20100101%20Firefox%2F128.0; woodmart_recently_viewed_products=45844|43824|12345|12352|43949|30024|12925|38383|30007|30011|42416|12383|30004|12601|29937|12179|12200|12197|12206|12203|12151|12209|38686|30479|30815|30840|30824|30832|38374|31697|38444|29721|31977|45993|29720|31974|29724|29722|29725|32502|12047|12327|30291|32495|47662|30281|11414|11411|12395|12405|12350; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpetcity.cl%2Ftienda%2Fbravecto-20-40kg%2F",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
    "TE": "trailers"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

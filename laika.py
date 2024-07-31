import http.client

conn = http.client.HTTPSConnection("api-cl.laika.com.co")

payload = "{\"operationName\":\"ProductDetail\",\"variables\":{\"addressId\":null,\"slugCity\":\"santiago-chile\",\"slugProduct\":\"apoquel-16-mg-20-tab\",\"ad\":0},\"query\":\"query ProductDetail($slugCity: String!, $slugProduct: String!, $addressId: Int, $ad: Int) {\\n  detail_product_mw(\\n    slug_city: $slugCity\\n    slug_product: $slugProduct\\n    address_id: $addressId\\n    ad: $ad\\n  ) {\\n    slug_error {\\n      city {\\n        id\\n        name\\n        __typename\\n      }\\n      error\\n      __typename\\n    }\\n    products_interest {\\n      id\\n      name\\n      slug\\n      is_available\\n      slug_pet\\n      brand {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      subcategory {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      category {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      references {\\n        id\\n        sku\\n        reference\\n        sale_price\\n        price_with_discount\\n        stock\\n        show_first\\n        status_id\\n        is_member\\n        saving_member\\n        savings_promotions\\n        can_request_notification\\n        min_buy_qty\\n        max_buy_qty\\n        weight\\n        laika_coins {\\n          cashback\\n          cashback_money\\n          active\\n          value\\n          __typename\\n        }\\n        laika_member {\\n          membership {\\n            id\\n            name\\n            benefits\\n            original_value\\n            value\\n            image\\n            acquired\\n            final_date\\n            start_date\\n            total_monthly_savings_member\\n            total_savings_member\\n            value\\n            value_monthly\\n            kit {\\n              id\\n              name\\n              sale_price\\n              references {\\n                id\\n                product_id\\n                sale_price\\n                price_with_discount\\n                kit_membership\\n                stock\\n                reference_images {\\n                  url\\n                  __typename\\n                }\\n                __typename\\n              }\\n              brand {\\n                id\\n                name\\n                __typename\\n              }\\n              subcategory {\\n                id\\n                name\\n                slug\\n                __typename\\n              }\\n              category {\\n                id\\n                name\\n                slug\\n                __typename\\n              }\\n              __typename\\n            }\\n            membership_variables {\\n              variable {\\n                id\\n                name\\n                __typename\\n              }\\n              variable_id\\n              value\\n              is_primary\\n              __typename\\n            }\\n            __typename\\n          }\\n          price\\n          percent_member\\n          __typename\\n        }\\n        reference_images {\\n          url\\n          url_raw\\n          __typename\\n        }\\n        promotion {\\n          id\\n          value\\n          __typename\\n        }\\n        membership {\\n          name\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    complementary_products {\\n      id\\n      name\\n      slug\\n      is_available\\n      slug_pet\\n      brand {\\n        id\\n        name\\n        __typename\\n      }\\n      subcategory {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      category {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      references {\\n        id\\n        sku\\n        reference\\n        sale_price\\n        price_with_discount\\n        stock\\n        show_first\\n        status_id\\n        is_member\\n        can_request_notification\\n        saving_member\\n        savings_promotions\\n        min_buy_qty\\n        max_buy_qty\\n        weight\\n        laika_coins {\\n          cashback\\n          cashback_money\\n          active\\n          value\\n          __typename\\n        }\\n        laika_member {\\n          membership {\\n            id\\n            name\\n            benefits\\n            original_value\\n            value\\n            image\\n            acquired\\n            final_date\\n            start_date\\n            total_monthly_savings_member\\n            total_savings_member\\n            value\\n            value_monthly\\n            kit {\\n              id\\n              name\\n              sale_price\\n              references {\\n                id\\n                product_id\\n                sale_price\\n                price_with_discount\\n                kit_membership\\n                stock\\n                reference_images {\\n                  url\\n                  __typename\\n                }\\n                __typename\\n              }\\n              brand {\\n                id\\n                name\\n                __typename\\n              }\\n              subcategory {\\n                id\\n                name\\n                slug\\n                __typename\\n              }\\n              category {\\n                id\\n                name\\n                slug\\n                __typename\\n              }\\n              __typename\\n            }\\n            membership_variables {\\n              variable {\\n                id\\n                name\\n                __typename\\n              }\\n              variable_id\\n              value\\n              is_primary\\n              __typename\\n            }\\n            __typename\\n          }\\n          price\\n          percent_member\\n          __typename\\n        }\\n        reference_images {\\n          url\\n          url_raw\\n          __typename\\n        }\\n        promotion {\\n          id\\n          value\\n          __typename\\n        }\\n        membership {\\n          name\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    product {\\n      id\\n      name\\n      slug\\n      is_available\\n      benefit\\n      feature\\n      description\\n      is_available\\n      slug_pet\\n      brand {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      subcategory {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      category {\\n        id\\n        name\\n        slug\\n        __typename\\n      }\\n      references {\\n        id\\n        sku\\n        reference\\n        sale_price\\n        price_with_discount\\n        stock\\n        show_first\\n        is_member\\n        status_id\\n        can_request_notification\\n        saving_member\\n        savings_promotions\\n        min_buy_qty\\n        max_buy_qty\\n        weight\\n        laika_coins {\\n          cashback\\n          cashback_money\\n          active\\n          value\\n          __typename\\n        }\\n        laika_member {\\n          membership {\\n            id\\n            name\\n            benefits\\n            original_value\\n            value\\n            image\\n            acquired\\n            final_date\\n            start_date\\n            total_monthly_savings_member\\n            total_savings_member\\n            value\\n            value_monthly\\n            kit {\\n              id\\n              name\\n              sale_price\\n              references {\\n                id\\n                product_id\\n                sale_price\\n                price_with_discount\\n                kit_membership\\n                stock\\n                reference_images {\\n                  url\\n                  __typename\\n                }\\n                __typename\\n              }\\n              brand {\\n                id\\n                name\\n                __typename\\n              }\\n              subcategory {\\n                id\\n                name\\n                slug\\n                __typename\\n              }\\n              category {\\n                id\\n                name\\n                slug\\n                __typename\\n              }\\n              __typename\\n            }\\n            membership_variables {\\n              variable {\\n                id\\n                name\\n                __typename\\n              }\\n              variable_id\\n              value\\n              is_primary\\n              __typename\\n            }\\n            __typename\\n          }\\n          price\\n          percent_member\\n          __typename\\n        }\\n        reference_images {\\n          url\\n          url_raw\\n          __typename\\n        }\\n        promotion {\\n          id\\n          value\\n          __typename\\n        }\\n        membership {\\n          name\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\"}"
#lol
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0",
    'Accept': "*/*",
    'Accept-Language': "en-US,es-CL;q=0.7,en;q=0.3",
    'Accept-Encoding': "gzip, deflate, br",
    'Referer': "https://laikamascotas.cl/",
    'content-type': "application/json",
    'api-key-client': "$2y$10$DAtaTvXcuyIXd.sWT0gnLueKF0U83Cu49XxAdhQQBg0ytoTR4dd/u",
    'Origin': "https://laikamascotas.cl",
    'Connection': "keep-alive",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "cross-site"
    }
# //Hola

conn.request("POST", "/web", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
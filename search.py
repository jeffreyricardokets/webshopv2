from models import *
import products

from autocorrect import Speller

Word = Speller(lang='en')


def add_query_item_to_list(query, tag_query, product_id_list):
    for item in query:
        product_id_list.append(item.product_id)
    for item in tag_query:
        product_id_list.append(item.product_id)
    return product_id_list

#find out if the
def run_search_query(term):
    tag_query = (Tag_for_products.select(Tag_for_products).join(Tags).where(Tags.tag_name ** term))
    query = (Products.select().where(Products.product_name ** term |
    Products.product_description ** term ))
    return query, tag_query

def search(term):
    product_id_list =[]
    query, tag_query =  run_search_query(term)
    if (query.exists() or tag_query.exists()):
        product_id_list = add_query_item_to_list(query, tag_query, product_id_list)
    else:
        converted_term = Word(term)
        print(converted_term)
        query, tag_query =  run_search_query(converted_term)
        if (query.exists() or tag_query.exists()):
            print(f'Could not find the item in the database with term {term}')
            print(f'We searched with term {converted_term} and found the following')
            product_id_list = add_query_item_to_list(query, tag_query, product_id_list)
        else:
            print('could find nothing at all')
    products.product_list_to_table(product_id_list)        

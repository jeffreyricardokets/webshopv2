from models import *
from rich.console import Console
from rich.table import Table

console = Console()

def create_tag(name, description):
    #find out if tag is already in our database
    query = Tags.select().where(Tags.tag_name == name)
    
    if query.exists():
        print('tag already exist use one with a different name')
    else:
    #create tag
        tag = Tags.create(tag_name = name) 
        print(f'Created a tag with name : {tag.tag_name}')

def product_add_tag(product_id, tag_id):
    product_query = Products.select().where(Products.product_id == product_id)
    tag_query = Tags.select().where(Tags.id == tag_id)
    Tag_for_products_query = Tag_for_products.select()
    
    if tag_query.exists() and product_query.exists():
        product = Products.get(Products.product_id == product_id)
        tag = Tags.get(Tags.id == tag_id)
        test_query = Tag_for_products.select().where(Tag_for_products.product_id == product.product_id ,Tag_for_products.product_tag_id == tag.id)
        if test_query.exists():
            return console.print('tag already added to this product' , style='bold red')
        else:
            Tag_for_products.create(product_id = product , product_tag_id = tag)
            return console.print('tag has been paired with the product', style='bold green')
    else:
        console.print('Error: something went wrong', style='bold red')

def list_products_per_tag(tag_id):
    table = Table(title='Product list that is connect to the tag id')
    query = Products.select().join(Tag_for_products).where(Tag_for_products.product_tag_id == tag_id)
    if query.exists():
        table.add_column('Product id')
        table.add_column('Product name')
        table.add_column('Product stock')
        for item in query:
            table.add_row(str(item.product_id),item.product_name,str(item.product_stock))
        console.print(table)
    else:
        print('could not find the tag')

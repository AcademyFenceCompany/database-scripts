import pandas as pd

# PRODUCT SCHEMA AND MAPPING TO NEW DATABASE

# products_df = pd.DataFrame(columns=['product_id', 'product_name', 'item_no', 'price_per_unit', 'shippable', 'family_category_id', 'description'])
# product_details_df = pd.DataFrame(columns=['product_details_id', 'product_id', 'size1', 'size2', 'size3', 'style', 'speciality', 'material', 'spacing', 'color', 'coating'])
# shipping_details_df = pd.DataFrame(columns=['shipping_details_id', 'product_id', 'weight', 'shipping_length', 'shipping_width', 'shipping_height', 'shipping_class', 'description'])
# product_media_df = pd.DataFrame(columns=['product_media_id', 'product_id', 'general_image', 'small_image', 'large_image'])

# loop that runs jobs parallel 
# - one for inserting data into product table
#           product_id?
#           product_name
#           desc_short/long?
#           item_no
#           price-cost
#           shipable
# - second for pairing that product (BY ID) with it's details in product_details table
#           color
#           size
# - third for product media (images)
#           img_small
#           img_large
# fourth for shipping details
#           weight_lbs
#           ship_length
#           ship_width
#           ship_height
#           class
# Starting with fence slats - cat id 42 (but that doesnt matter anyways bc all fence slat products cat_id_fk are NULL in the database :))

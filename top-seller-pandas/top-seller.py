#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:28:11 2020

@author: Sardor
@version: 1.0.0
@python_v: 3.7
"""

import argparse
import datetime # input validation: min_date, max_date
import os
import pandas as pd

SCRIPT_DESC = """Python script that finds and prints:
- top seller n products in given date range (product name & quantity)
- top seller n stores in given date range (store name & quantity)
- top seller n brands in given date range (brand & quantity)
- top seller n cities in given date range (city & quantity)
"""
DEFAULT_TOP = 3
DEFAULT_MIN_DATE = "2020-02-01"
DEFAULT_MAX_DATE = "2020-06-30"
        

def print_top_seller(top_seller, df_merged, df_cols=['name', 'quantity'],
                     group_by='name', top=DEFAULT_TOP):
    print('-- top seller %s --' % top_seller)
    df = df_merged[df_cols].groupby(by=[group_by], sort=False,
                  as_index=False).sum()
    df = df.nlargest(n=top, columns=df_cols[-1], keep='all')
    print(df.to_string(index=None),'\n')
    
    
def main(args):
    path = args.path
    min_date = args.min_date
    max_date = args.max_date
    top = args.top
    
    df_products = pd.read_csv(os.path.join(path,'product.csv'))
    df_sales = pd.read_csv(os.path.join(path,'sales.csv'))
    df_stores = pd.read_csv(os.path.join(path,'store.csv'))
    
    # sort sales by date
    df_sales = df_sales.sort_values(by='date')
    
    # filter sales by given date
    after_start_date = df_sales["date"] >= str(min_date)
    before_end_date = df_sales["date"] <= str(max_date)
    between_two_dates = after_start_date & before_end_date
    df_sales = df_sales.loc[between_two_dates]
    
    # product and brand
    df_product_quantity = df_sales[['product', 'quantity']]
    df_prd_qnt_merged = df_product_quantity.merge(df_products.set_index('id'),
                                                  left_on='product',
                                                  right_index=True)
    print_top_seller(top_seller='product', df_merged=df_prd_qnt_merged,
                     df_cols=['name','quantity'], group_by='name', top=top )
    print_top_seller(top_seller='brand', df_merged=df_prd_qnt_merged,
                     df_cols=['brand','quantity'], group_by='brand', top=top )
    
    # store and city
    df_store_quantity = df_sales[['store', 'quantity']]
    df_store_qnt_merged = df_store_quantity.merge(df_stores.set_index('id'),
                                              left_on='store',
                                              right_index=True)
    print_top_seller(top_seller='store', df_merged=df_store_qnt_merged,
                     df_cols=['name','quantity'], group_by='name', top=top )
    print_top_seller(top_seller='city', df_merged=df_store_qnt_merged,
                     df_cols=['city','quantity'], group_by='city', top=top )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=SCRIPT_DESC,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-p', '--path', type=str, default='',
                        help='path to input csv files:\n' +
                             'sales.csv, product.csv, store.csv\n'+
                             'Default: current dir')
    parser.add_argument('-s', '--min-date', type=datetime.date.fromisoformat,
                        default=DEFAULT_MIN_DATE,
                        help='start of the date range.\n' +
                             'Default: %s' % DEFAULT_MIN_DATE)
    parser.add_argument('-e', '--max-date', type=datetime.date.fromisoformat,
                        default=DEFAULT_MAX_DATE,
                        help='end of the date range.\n' +
                             'Default: %s' % DEFAULT_MAX_DATE)
    parser.add_argument('-t', '--top', type=int,
                        default=DEFAULT_TOP,
                        help='number of rows in the output.\n' +
                             'Default: %s' % DEFAULT_TOP)
    main(parser.parse_args())

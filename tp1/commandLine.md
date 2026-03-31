# total sale by category
cat purchases.txt | ./tp1/mapper_by_category.py | sort | ./reducer.py

# total sales for specific category ex : Toys 
cat purchases.txt | ./tp1/mapper_by_category.py | sort | ./reducer.py | grep "Toys"

# minimum sales by store
cat purchases.txt | ./mapper.py | sort | python3 ./tp1/min_sell_by_store.py

# specific min sales by store
cat purchases.txt \
  | ./mapper.py \
  | sort \
  | ./tp1/min_sell_by_store.py
  | grep "Reno"

# sell sum by day of the week 
cat purchases.txt \
  | ./tp1/mapper_sum_by_day.py \
  | sort \
  | ./reducer.py

# sell mean by day of the week
cat purchases.txt \
  | ./tp1/mapper_sum_by_day.py \
  | sort \
  | .tp1/avg.py 
python src/db_to_script.py

# delete database files after converting
find -iname "*\.db*" | xargs rm -rf

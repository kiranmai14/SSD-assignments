#!/bin/bash
mkdir temp_activity
cd temp_activity
touch temp{1..50}.txt
for file in temp{1..25}.txt
do
  mv "$file" "${file%.txt}.md"
done
for file in *
do
  ext=${file##*.}
  new=${file%.*}
  mv "$file" "${new}_modified.$ext"
done
zip txt_compressed.zip *.txt


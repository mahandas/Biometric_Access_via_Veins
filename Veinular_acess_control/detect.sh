##############
##
##automation script
##
##############
now=$(date "+%Y.%m.%d")
cd data_store/meta_storage
num=$(ls -1 | wc -l)
echo "no. of files in meta storage = $num"
#num=$((num+1))
cd ..
cd ..

python rpi_cam2.py
python process2.py
mv temp.jpg data_store/meta_storage

cd data_store/meta_storage
python matching.py $num
val=$(cat match.txt)
rm temp.jpg
rm match.txt
echo "access granted to $val"
cd ..
cd "$val"
ls 
read wait




##############
##
##automation script
##
##############
now=$(date "+%Y.%m.%d")
cd data_store/meta_storage
num=$(ls -1 | wc -l)
echo "no. of files in meta storage = $num"
cd ..
cd ..
echo "enter name:- "
read name
python rpi_cam1.py
python process1.py
python fast.py
cd data_store
mkdir "$num"
cd "$num"
mkdir "$name"
cd ..
cd ..
rm temp.jpg
mv this.jpg $num.jpg
mv $num.jpg data_store/meta_storage
mv *.jpg data_store/"$num"/"$name"/
mv keypoints.txt data_store/"$num"/"$name"/



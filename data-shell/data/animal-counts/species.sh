#Script to find unique species in each file
#Usage: bash species.sh one_or_more_filenames

for file in $@
do
echo "Unique species in $file: "
cut -d , -f 2 $file | sort | uniq
done

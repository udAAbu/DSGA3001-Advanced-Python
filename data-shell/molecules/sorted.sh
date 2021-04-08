#Sort files by their line number
#Usage: bash sorted.sh one_or_more_filenames
wc -l $@ | sort -n


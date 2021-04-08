for f in nbody_[1-4].py; 
do 
python -m cProfile -s cumulative $f >> log.txt; 
done

echo "initialisation de script"
PARAM1=$1
PARAM2=$2
PARAM3=$3
printf "parametre reçu 1 =$PARAM1 \n"
printf "parametre reçu 2 =$PARAM2 \n"
printf "parametre reçu 3 =$PARAM3 \n"

printf "execution script python"
python3 ./folderpython1/packagetest/test1.py -a $PARAM1 -b $PARAM2 
printf "exit fin script \n"


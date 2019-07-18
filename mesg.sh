#!/bin/bash

########### get alert Data##############
declare -i cnt=0 
lynx -dump $1  | sed -n "/$2/,/Display/p" | sed "1,/$3:/!d"  | sed '1d;$d'  > /tmp/w.buf
# lynx -dump $1  | sed -n '/Weather warnings/,/Display/p' | sed '1,/Caption:/!d'  | sed '1d;$d' > w.buf
input="$(cat /tmp/w.buf | grep .jpg )"
#echo $input
while IFS= read -r LINE
do
################## extracts alerts ################

SPLIT="$(echo $LINE | tr -d '[]' | tr -d '[:space:]')"

cat /tmp/w.buf | sed -n "/$SPLIT/, $ p" | head -3 | sed '1d;2d' > /tmp/tmp.w  


input2="$(cat /tmp/tmp.w)"
if [ -z "$input2" ]
then
      echo "....."
else

############## process alerts ################

if  [ $cnt == 0 ]
then
((cnt++))
cat /tmp/w.buf | sed -n "/$4/,/^ *$/p" | awk '!seen[$1,$2]++' | sed '1d'

fi
#echo $input2 

fi
done  <<< "$input"

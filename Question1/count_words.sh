#!/bin/bash
helpFunction()
{
   echo ""
   echo 'i.e: Usage: count_words.sh -f ./words.txt '
   echo -e "\t -f: Your file Path"
   exit 1
}

Count_your_words()
{
    document=`cat "$INPUT"`
    echo "$document" | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr ' ' '\n' | grep -v '^$' | sort | uniq -c | sort -nr | head -n 1

}

while getopts "f:" opt
do
   case "$opt" in
      f ) INPUT="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$INPUT" ]
   then 
        echo "Please specific your file path";
        helpFunction
    else
        Count_your_words
fi
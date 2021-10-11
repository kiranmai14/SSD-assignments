#!/bin/bash
contains () {
    search=$1; shift
    yes=1
    for arrele
    do
        if [[ $arrele == "$search" ]] 
        then
            yes=0
            break
        fi
    done
    return $yes
}
q=$( (echo $1 | grep -o . | sort |tr -d '\n') )
comm=($(compgen -c | sort | uniq))
arr=($(compgen -c | grep -o . | sort | uniq))
flag3=0
flag2=0
flag1=0
declare -A ch
declare -A ans
for i in ${arr[@]}
do
     ch[$i]=0;
done
for (( i=0; i<${#q}; i++ ))
do
	var=${q:i:1}
	r=($( contains "$var" "${arr[@]}" && echo 1 || echo 0 ))
	if [[ $r -eq 1 || $q == ']]' ]];
	then
	    ((ch[$\var]+=1))
	else
	    flag1=1
	    break
	fi  
done
if [[ flag1 -eq 1 ]]
then
    echo "NO"
    exit
fi
for k in "${comm[@]}"
do
    declare -A res
    for i in ${arr[@]}
    do
        res[$i]=0;
    done
	for (( i=0; i<${#k}; i++ ));
	do
	    var=${k:i:1}
	    ((res[$\var]+=1))
	done
	flag2=0
	for i in ${arr[@]}
    do
        if [[ ch[$\i] -ne res[$\i] ]] 
        then
            flag2=1
            break 
        fi
    done
    if [[ flag2 -eq 0 ]]
    then
        ans+='\t'
        ans+=$k
        flag3=1
    fi        
done
if [[ flag3 -eq 0 ]]
then
    echo -e "NO"
else
       printf 'YES'
       for (( i=0; i < ${#ans[@]}; i++ ))  
       do
          echo -e ${ans[$i]}
       done
fi
 

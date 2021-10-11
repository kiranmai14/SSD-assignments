#!/bin/bash
declare -A ch
declare -A num
j=0
for i in 'M' 'CM' 'D' 'CD' 'C' 'XC' 'L' 'XL' 'X' 'IX' 'V' 'IV' 'I'
do
    ch[$j]=$i
    ((j=j+1))
done
j=0
for i in 1000 900 500 400 100 90 50 40 10 9 5 4 1
do
    num[$j]=$i
    ((j=j+1))
done
declare -A rep
rep=([I]=1 [V]=5 [X]=10 [L]=50 [C]=100 [D]=500 [M]=1000)
int=0
rom=""
res1=""
integerToRoman(){
    str=""
    n=0
    q=0
    i=0
    while (( $int>0 ))
    do
        n=${num[$i]}
        str=${ch[$i]}
        ((q=int/n))
        ((int=int%n))
        while (( $q>0 )) 
        do
            res1=$res1$str
            ((q--))
        done
        ((i++))  
    done
}
res2=0
romanTointeger1(){
    s1=0
    p=""
    k=0
    rom=($(echo ${rom1[@]} | grep -o .))
    for (( i=0; i<${#rom[*]}; i++ ));
	do
        p=${rom[$i]}
        s1=${rep[$p]}
        ((k=i+1))
        if (( k<${#rom[*]} ))
        then
            p=${rom[$k]}
            s2=${rep[$p]}
            if (( s1>=s2 ))
            then
                ((res2=res2+s1))
            else
                ((res2=res2+s2-s1))
                ((i++))
            fi
        else
            ((res2=res2+s1))
        fi
    done
}
res3=0
romanTointeger2(){
    s1=0
    p=""
    k=0
    rom=($(echo ${rom2[@]} | grep -o .))
    for (( i=0; i<${#rom[*]}; i++ ));
	do
        p=${rom[$i]}
        s1=${rep[$p]}
        ((k=i+1))
        if (( k<${#rom[*]} ))
        then
            p=${rom[$k]}
            s2=${rep[$p]}
            if (( s1>=s2 ))
            then
                ((res3=res3+s1))
            else
                ((res3=res3+s2-s1))
                ((i++))
            fi
        else
            ((res3=res3+s1))
        fi
    done
}
if [ "$#" -eq 1 ] 
then
    int=$1
    if (( $int>0 ))
    then
        integerToRoman
        echo $res1
        exit
    fi
fi
x1=0
x2=0
if [ "$#" -eq 2 ] 
then
    rom1=$1
    rom2=$2
    if [[ -n ${rom1//[0-9]/} ]]
    then
        romanTointeger1
        x1=$res2
        romanTointeger2
        x2=$res3
        echo $((x1+x2))
        exit
    else
        ((rom=$1+$2))
        int=$rom
        integerToRoman
        echo $res1
        exit
    fi
fi


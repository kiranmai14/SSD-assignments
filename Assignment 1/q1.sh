#!/bin/bash
du -sh */ | sort -rh |awk '{$2=substr($2,1,length($2)-1); print $2,"\t",$1}' 

#!/bin/bash
cat $1| tr A-Z a-z |grep -o "[^ ]*ing\b" > $2

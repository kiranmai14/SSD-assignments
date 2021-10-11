# Assignment-1:Bash Scripting
---
#### Software Systems Development

##### Answer 1

1) a) **du** command will list all the directories with their sizes.**-h** will give size in human readable form. **-s** option will summarize each argument. /* will list all directories in current directory.
 b) Directories are sorted using **sort** command where **-r** option sorts in reverse order of their sizes, **-h** will do human numeric sort.**awk** command and **substr** method are used to remove the trailing backslash ( / ).

---
##### Answer 2

2) a) **$1** will contain input.txt which is first argument.**$2** will contain output.txt which is second argument.
b) **$1** which is input.txt file contains some random text.**cat** command will pipe the text to **tr** command. **tr** command will translate text from uppercase (if contains uppercase characters) to lowecase.
c) **grep** will match the text with regular expression. **-o** option will print  only  the  matched  (non-empty) parts of a matching line,with each such part on a separate output line.
---
##### Answer 3

3) a) **$1** will contain string which is first argument.
b) **compgen -c** is used to get all the bash commands.**sort** command will sort the bash commands.**uniq** will give only the commands which are unique.The query string is splitted into characters. In the for loop each bash command is splitted into characters.The count of the characters of the query string and bash command are checked.b)a) If the count is same, the commands are added to the 'ans' variable. 'YES' is printed followed by the resulting bash commands.b)b) Else 'NO' is printed. In addition to that if the user inputs any query string in which the query string's character does not contain in any of the bash commands charactes then also 'NO' is printed.For example if '$abc' is given as input then 'NO' will be printed since '$' is not there as a bash commands character.
c) As the commands are being sorted, variable 'ans' will contains resulting commands in the sorted order and they are printed.
---
##### Answer 4

4) a) Count of the arguments is checked.If the count of arguments is equal to one integerToRoman function is called.integerToRoman function will convert the given number to roman number.
b) **$#** will check the count of the arguments.If the count of arguments is equal to two then the first argument is checked using **rom1//[0-9]/**.This expression will give false if the input is integer.Then the two integers are added and integerToRoman function is called.
c) **rom1//[0-9]/** will return true if the input is other than an integer.Then the two roman numbers are converted to integers using romanToInteger1 and romanToInteger2 functions.The resulting integers are added.
---
##### Answer 5

5) a) **mkdir** will create a new directory with the given name. **cd** command is used to move into temp_activity directory.
b) **touch** command will create empty files. Using **touch** and **temp{1..50}.txt** temp1.txt,temp2.txt.....temp50.txt are created at a time.
c) for loop and **mv** command are used to change the extension from **.txt** to **.md**
d)a) using file##*. extension of the file is extracted. using file%. file name is extracted. In the **mv** command file name is appended with _modified and extension is added to get the new file name.d)b)using **zip** command the text files are zipped into the given folder
---


   


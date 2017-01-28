## About this repository
  Finds duplicate files in the given path and dumps the result in a csv file. The csv file will have hash, files list and size of the file

#### How to execute:
  ```
  python findDuplicate.py
  ```
  Once you run the program it will ask for the directory to analyze for duplicate file. Then you will be asked for the report file name.
  
#### Result file:
The result will be saved in the below format,<br>

| `hash` | `files`  | `size (in bytes)`|
| -----| -----| -----|
| f4e740fa9511c9cee1409e0f5ef1fcba| file_name_1<br>file_name_2| 34567938|
| ...| ...| ...|

Note: Works with python 2.7.x

##### Upcoming Features :)

Prints the total size of found duplicated files
Keep the first file in each cell in second column(refer above table) and delete the rest

# how-to git and use commandline
---
## Overview
Why we care, what this will allow us to do, etc...

### Estimated Time Cost: 0.5 hrs 

### Prerequisites:

Have a terminal

1. Clone remote repo into local
    
    ```
    $ git clone ssh://git@github.com/[username]/[repository-name].git <directory name, optional>
    ```
    - This uses ssh, you can also use html
    - The directory does not have to exist prior
2. Do things in your local repo
    - What is there to do in your repo?
        
        ```
        $ git rm or $ git rm -r
        ```
        - Remove files, or directories
        
        ```
        $ cp <filename> <file/path> or cp -r <filename> <file/path
        ```
        - Copy files or directories
        
        ```
        $ mv <filename> <newfilename>
        ```
        - mv moves a file if you add a path as the second argument. However, it can also be used to rename a file, which is what happens above 
3. Stage changes
    
    ```
    $ git status
    ```
    - Check what needs to be staged
    
    ```
    $ git restore <filename> or $ git restore --staged <filename>
    ```
    - Unstage or discard changes, depending on the status of the file
    
    ```
    $ git add <filename>
    ```
    - Stages changes to be commited 
    - There are many different '''$ git add''' commands
4. Commit changes
    
    ```
    $ git commit -m "<message>"
    ```
    - commits all previously staged changes, messages show up in version history
5. Push changes
    
    ```
    $ git push
    ```
    - Pushes all changes staged from local to remote repo


### Resources

---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Brian, pd2  
Vansh, pd2  
Weichen, pd2

# File Renamer

### Rename files based on a text file

This idea was originated when I downloaded multiple video lectures and happened that their names were not properly configured.

The videos were named with the following pattern:   
> video1.mp4  
> video2.mp4  
> ...     
> video160.mp4

Luckily enough, there was a text file provided with all the names inside, one name per line.

The script was created to avoid renamining all the video files manually, by extracting them from the text file.

# Demo

### Before

  
>  $ ls -l E:/Test/   
>  total 69545    
>  -rw-r--r-- 1 lucas 197609       45 May 11 20:51 FileNames.txt      
>  -rw-r--r-- 1 lucas 197609 48999579 Apr  7 20:54 video1.mp4     
>  -rw-r--r-- 1 lucas 197609 18565028 Apr  7 23:04 video2.mp4     
>  -rw-r--r-- 1 lucas 197609  3643500 Mar 15 12:26 video3.mp4     
> 
> $ cat E:/Test/FileNames.txt     
> Introduction    
> Body/Develop    
> Ending: The end     


### Running the script
> $ python renamer.py 
> 
> Welcome to File-Renamer
> 
> Select files path: E:/Test/     
> Select name file: E:/Test/FileNames.txt     
> Select name pattern: video      
> Select file extension: .mp4     
> 
> Type 'yes' to see a preview of final result: yes  
> The file video1.mp4 will be renamed to: 1 - Introduction.mp4    
> The file video2.mp4 will be renamed to: 2 - Body-Develop.mp4    
> The file video3.mp4 will be renamed to: 3 - Ending - The end.mp4    
> 
> Type 'yes' to confirm rename: yes
> 
> Rename was done.

### After
> $ ls -l E:/Test/    
> total 69545     
> -rw-r--r-- 1 lucas 197609 48999579 Apr  7 20:54 '1 - Introduction.mp4'      
> -rw-r--r-- 1 lucas 197609 18565028 Apr  7 23:04 '2 - Body-Develop.mp4'      
> -rw-r--r-- 1 lucas 197609  3643500 Mar 15 12:26 '3 - Ending - The end.mp4'      
> -rw-r--r-- 1 lucas 197609       45 May 11 20:51  FileNames.txt      

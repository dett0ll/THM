docker image file

 
<img width="940" height="296" alt="image" src="https://github.com/user-attachments/assets/1294bf27-e4c4-47a1-95d5-4cabd49c2a7e" />

docker build.

Creates image from the custom image file 
 

From the above SS we can see the docker image file name (d7e132b77f83c2a0642452dcef7f44d83827ce7c9a07cb9aa351ed7f0b19837e)

Lets run the image

docker run d7e132b77f83c2a0642452dcef7f44d83827ce7c9a07cb9aa351ed7f0b19837e

 

However there is an issue. We started a container but we cannot see our nodejs server
 

So, the issue is with running the container.
instead of using docker run d7e132b77f83c2a0642452dcef7f44d83827ce7c9a07cb9aa351ed7f0b19837e

use docker run –p 3000:3000 d7e132b77f83c2a0642452dcef7f44d83827ce7c9a07cb9aa351ed7f0b19837e

 
 


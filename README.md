TODO: Number of iterations Parameter Field on Profile page along with Upload button  
Password change



NOTE-  
1. This app is free to use while it is in the development phase.
2. Since, the app is not yet used for commercial purposes, the user can input songs by himself.
3. The app creates a karaoke of the song the user uploads. (There is a limit to the length of the song for now which is 1 minute and the only formats allowed are mp3 and wav. Also the quality of the karaoke can be controlled based on the requirements.)  
4. Since the generation of karaoke requires heavy processing, we request the user to revisit us after he gets an email from us about the successful karaoke generation.
5. If the user inputs a song whose karaoke is already generated, he gets the email instantly( handled via hashing).

Usage-

(Free Triall)
1. Once the user clicks on the "TRY FOR FREE" button on the homepage, he is redirected to the upload page where he can upload a song and provide an email address.  
2. Once the karaoke for the song is generated, the user gets an email notification. The user is then required to click on the link in the email and input his credentials and proceed to the singing page.  
3. The singing page has a calibration tool embedded (called Rms) for calibrating the user’s microphone and also the noise control for the song(This step is crucial since microphone thresholds vary from device to device. Also the noise levels depend upon the type of song the user inputs).  
4. On the singing page the karaoke starts to play after 5 seconds so the user is expected to grant the microphone access as prompted on the page in time.  
5. The user is then required to sing along with the karaoke (using headphones so that we can clearly evaluate). The user can see his pitch plot and karaoke's pitch plot in real time.  
6. The user can try singing multiple times simply by clicking on "RETRY" button the page singing page.  
7. After the user is satisfied and presses the "proceed" button, he is redirected to the leaderboard page where he can see his scores along with the scores of people who sang the same song.      

(Pseudo Paid Version)
1. The user is required to sign up on the home page by providing a username and his first name, last name, email-id and password (the username being unique) or login if he is already registered.  
2. The user is then redirected to his profile page. Here he can upload a new song(gets an email after successful karaoke generation) and view all his previously uploaded songs.(TODO:karaoke number of iterations)
3. He can perform the following actions-  
Download Karaoke - The user can click on this button to download the karaoke of a song he uploaded.  
Sing - The user can click on this button to open the singing page where he can sing and get his dynamic graph for the song.  
Score History - The user can click on this button to get a graph of his scores for a particular song. He can analyse his singing scores for the song and track his improvement.  
4. Leaderboard - The user can click on this button to directly open the leaderboard for a song.


Citations-
Karaoke - http://www.durrieu.ch/research/jstsp2010.html
Pitch Detection - https://github.com/cwilso/pitchdetect
Dynamic Graph - https://github.com/shutterstock/rickshaw
Design - https://github.com/twbs/bootstrap
Jquery - https://github.com/jquery/jquery
Wallpapers - pexels.com
Demo Song - Tujhe Sochta Hoon (Sony Music Entertainment India Pvt. Ltd)


Youtube Demo Link - https://youtu.be/iwKzN4ybRDM



# MUSIC PLAYER CONNECTED WITH MQTT



## Setup:

1.  Install requirements
   
   ```bash
   pip3 install -r requirements.txt
   ```

2. edit config.py file
   
   1. Set mqtt broker address
   
   2. Set mqtt user
   
   3. Set mqtt password
   
   4. Set device__name
      
         

## Run the start the player

```bash
./main.py
```



## PLAYER COMMAND



### Command syntax

```
command-name.args
```

## COMMANDS

1. play.{song-name} >> PLAY A SONG NAMED LIKE {song-name}

2. stop 

3. pause 

4. resume

5. next

6. previous

7. vol-up

8. vol-down

9. set-vol.{volume_val} >> SET VOLUME 

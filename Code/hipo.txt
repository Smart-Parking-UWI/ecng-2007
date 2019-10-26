# A

### REGION SELECTION
***
START 
CONNECT to video stream
if  not end of region 
    PROMPT ADMINSTRATOR to SELECT PARKING REGION from image 
    ADD PARKING REGION to REGION QUEUE
    OUTPUT  REGION List
if end 
    Next step
***

### SET CAR COUNT
***
START
FOR region in REGION_QUEUE{
    PROMPT ADMINISTRATOR to set REGION_CAPACITY
}
END
***

# AD

### IMAGE SAMPLING
***
Start
input region
CONNECT TO VIDEO STREAM
SAMPLE 10 IMAGES from region
ADD IMAGES TO A QUEUE
OUTPUT QUEUE
next step
end
***
### DETECT and Count CARS

***
Start

INPUT QUEUE OF SAMPLED IMAGES AND CURRENT CAR COUNT FROM DATABASE

FOR each IMAGE in QUEUE
    DETECT CARS
    COUNT CARS
    IF COUNTED CARS is EQUAL to CURRENT CAR COUNT;
        CONTINUE;
    ELSE
        UPDATE CURRENT CAR COUNT in DATA BASE;
*** 

# OD

***
BEGIN
Input data
  READ in input data from textfile
   IF input_data changes
     PRINT input_data to display
   ELSE
     PRINT input_data to display
 END
***
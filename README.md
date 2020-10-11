# photo_joint

-The result of stitching photos is:
 ![image](final.jpg)
 ![image](final2.jpg)

-Program description
 -lib: PIL, numpy, numexpr,
 -photo source: Photos are placed in the photos folder of the current directory by default
 -The previous photo: Defined in createNevImage, you can modify it yourself
 -alpha: modify the transparency of the previous photo, the default is 0.5, you can modify the test by yourself
 -photos: After running the code, several photos will be generated in the code directory, which are generated indirectly during running. The final photo is final.jpg
 -past.py past3.py: is the experimental code, corresponding to final2.jpg, fianl.jpg. The specific difference between the two codes is the different cascading method.
 You can see the comments in the code.
 -See the program description for details.


-note: The transfer function directly resets the size of the photo, so the photo will be deformed. Due to the proportion of cropping the photo may make the photo no longer coordinated.

-thanks: @the world has no truth

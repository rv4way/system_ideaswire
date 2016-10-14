# system_ideaswire
this module contains the following structure:-

  system_ideaswire
    -> add_src
    -> data
          -> add_image
          -> search_image
    -> img_rep
    -> model
    
  add_src folder conatin all the source code, test_server.py is api of this module written in flask using celery and redis.
      add_single.py call compare.py to calculate rep of the image and store it in pkl file to img_rep folder
      search_img.py call compare.py to calculate rep of the image, after generating rep it compute the distance from previously generated rep which is stored in pkl file. its return the min distance.
      
      the model folder contain the dlib face predictor file and torch neural net file.

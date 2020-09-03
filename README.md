Target : By using KNN classifier to predict the text in amazon captcha during webscrapping
Accuracy : 94 ~ 96%

1.Ideas:
  (i) There are 6 words in each captcha which included A,B,C,E,F,G,H,J,K,L,M,N,P,R,T,U,X,Y (totally 18 alphabets only) <br>
  (ii) Width of each word is around 26 ~27 units and the largest width of word is 33 units(M)
  (iii) All of them are in big capital letters
  (iv) Try to split them into six independent images and using trained KNN model to classify(predict) those words
 
2.Problems during spliting into six boxes:
  (i) Some of images are unable to be splitted into six boxes (least than six)
	Reasons : (a) width of some images are too small --> two or more alphabets are in one splitting images
	Solutions : Construct the width of images by ourself
  (ii) Some of images are unable to be splitted into six boxes (more than six)
	Reasons　: (a) there are some 'blank image' appear --> nothing in image
	Solutions : Drop it

3.Model features:
  By using HOG(Histrogram of oriented gradients) as input features
	reference :(a) https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html
		   (b) https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients

4.KNN Models:
  (i) I've tried several parameters k in KNN model and others parameters are default values.The accuraries are around 0.94% - 0.96% 
  (ii) Model is only able to predict one spliting word(one spliting image) at one times
  (iii) Input : Splitting Image with .png format(or you can change the format to .jpg but you need to modify the saving code in python by yourself)
  (iv) You can use the training_dataset to train your own KNN model (There are totally 588 captcha in datasets)

5.Failure of model:
  (i) There are some 'broken parts' in captcha , please refer the 'fail_to_classify' image
  (ii) The new classes appear 

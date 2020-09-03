Target : By using KNN classifier to predict the text in amazon captcha during webscrapping <br>
Accuracy : 94 ~ 96%

1.Ideas: <br> 
  (i) There are 6 words in each captcha which included A,B,C,E,F,G,H,J,K,L,M,N,P,R,T,U,X,Y (totally 18 alphabets only) <br>
  (ii) Width of each word is around 26 ~27 units and the largest width of word is 33 units(M) <br>
  (iii) All of them are in big capital letters <br>
  (iv) Try to split them into six independent images and using trained KNN model to classify(predict) those words <br>
 
2.Problems during spliting into six boxes: <br>
  (i) Some of images are unable to be splitted into six boxes (least than six) <br>
	Reasons : (a) width of some images are too small --> two or more alphabets are in one splitting images <br>
	Solutions : Construct the width of images by ourself <br>
  (ii) Some of images are unable to be splitted into six boxes (more than six) <br>
	Reasons　: (a) there are some 'blank image' appear --> nothing in image <br>
	Solutions : Drop it <br>

3.Model features: <br>
  By using HOG(Histrogram of oriented gradients) as input features <br>
	reference :(a) https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html <br>
		   (b) https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients <br>

4.KNN Models: <br>
  (i) I've tried several parameters k in KNN model and others parameters are default values.The accuraries are around 94% - 96%  <br>
  (ii) Model is only able to predict one spliting word(one spliting image) at one times <br>
  (iii) Input : Splitting Image with .png format(or you can change the format to .jpg but you need to modify the saving code in python by yourself) <br> 
  (iv) You can use the training_dataset to train your own KNN model (There are totally 588 captcha in datasets) <br>

5.Failure of model: <br>
  (i) There are some 'broken parts' in captcha , please refer the 'fail_to_classify' image <br>
  (ii) The new classes appear  <br>

# Card_Detection
   
   
### Produce_Dataset.py   
훈련용 데이터를 얻는 프로그램.
카드 종류에 따라 마지막 elif문의 이미지 이름을 바꿔서 저장해야 함.
실행시킨 후 카드가 올바르게 추출되고 있는 상태에서 Space Bar를 꾹 눌러 이미지 파일을 저장할 수 있음.
생성된 이미지 파일로 이후 csv파일을 이용해 dataset을 만듦.
   
   
### Make_CSV.py   
CSV파일을 만드는 프로그램.   
CSV파일은 훈련 dataset을 만들기 위한 엑셀파일로, 1열에는 이미지 파일명이, 2열에는 그에 해당하는 class(숫자)가 적혀있음.  
카드의 종류가 늘어남에 따라 for 문을 하나씩 추가해주어 파일 명과 그에 대응하는 class(숫자)를 수정해야 함.
실행하면 mycsv.csv 파일이 생김.
   
   
### CNN_Model.py   
모델을 구현하고 훈련시키는 프로그램.   
Custom_Dataset.py 프로그램을 import하여 mycsv.csv 파일로부터 dataset을 생성함. 
실행하면 훈련이 진행되며, 훈련을 마친 모델은 마지막 줄 save_checkpoint() 함수에 의해 my_checkpoint.pth.tar 파일에 저장됨.  
(주의: 구분이 필요한 카드 종류 수를 처음에 num_types 변수에 적어주어야 함.)
   
   
### Mahjong_Detection.py   
최종적으로 실시간으로 카드를 구별하는 프로그램. 
load_checkpoint() 함수를 이용해 my_checkpoint.pth.tar 파일에 저장된 학습된 모델을 불러옴.
카드의 종류가 늘어남에 따라 getContours() > for cnt in contours > if 5000>area>1000 > if objCor == 4 내부의 elif문을 추가해줘야 함.  
   
   
   
## 진행과정   
   
### 2021.03.13   
카드 종류 인식까지는 완료. 모든 카드 종류를 구분하는 건 시간문제일 듯.   
그런데 동일한 카드가 여러 개 있을 때 그 개수를 파악하는 건 아직 어떻게 해야할지 모르겠음.   
   

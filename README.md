# Mahjong_Detection

   
### Resource   
훈련용 데이터 저장.   
tong_one_{}.png ~ tong_nine_{}.png (통수패)   
sak_one_{}.png ~ sak_nine_{}.png (삭수패)   
man_one_{}.png ~ man_nine_{}.png (만수패)   
poong_dong_{}.png ~ poong_book_{}.png (동서남북)   
Baek_{}.png Bal_{}.png Choong_{}.png (백발중)   
   
!!상하 대칭이 아닌 이미지는 뒤집어진 이미지 데이터도 저장해야하며, 뒤집어진 데이터는 파일명에 _r 을 붙인다!!   
ex) man_seven_r_{}.png   
   
   
### Produce_Dataset.py   
훈련용 데이터를 얻는 프로그램.   
카드 종류에 따라 마지막 elif문의 이미지 이름을 바꿔서 저장해야한다. (이름은 위 Resource 참고)   
실행시킨 후 카드가 올바르게 추출되고 있는 상태에서 Space Bar를 꾹 눌러 이미지 파일을 저장할 수 있다.   
하나의 이미지 세트(sak_five_{}.png나 Choong_r_{}.png 등)에는 총 600장의 이미지 파일을 만든다. (가깝게, 보통 거리, 멀리 각각 200장씩)   
생성된 이미지 파일은 각각 폴더에 모아 Resource 폴더에 집어넣으며, 속의 내용물은 이후 csv파일을 이용해 dataset을 만들기 위해 Resource 폴더에 다 꺼내둔다.   
   
   
### Make_CSV.py   
CSV파일을 만드는 프로그램.   
CSV파일은 훈련 dataset을 만들기 위한 엑셀파일로, 1열에는 이미지 파일명이, 2열에는 그에 해당하는 class(숫자)가 적혀있다.   
카드의 종류가 늘어남에 따라 for 문을 하나씩 추가해주어 파일 명과 그에 대응하는 class(숫자)를 수정하면 된다.   
실행하면 mycsv.csv 파일이 생겨난다.   
   
   
### CNN_Model.py   
본격적으로 모델을 구현하고 훈련시키는 프로그램.   
Custom_Dataset.py 프로그램을 import하여 mycsv.csv 파일로부터 dataset을 생성한다.   
실행하면 훈련이 진행되며, 훈련을 마친 모델은 마지막 줄 save_checkpoint() 함수에 의해 my_checkpoint.pth.tar 파일에 저장된다.   
   
!!구분이 필요한 카드 종류 수를 처음에 num_types 변수에 적어주어야 한다!!
   
   
### Mahjong_Detection.py   
최종적으로 실시간으로 패를 구별해주는 프로그램.   
load_checkpoint() 함수를 이용해 my_checkpoint.pth.tar 파일에 저장된 학습된 모델을 불러온다.   
카드의 종류가 늘어남에 따라 getContours() > for cnt in contours > if 5000>area>1000 > if objCor == 4 내부의 elif문을 추가해준다.   
   
   
   
## 진행과정   
   
### 2021.03.13   
카드 종류 인식까지는 완료. 모든 카드 종류를 구분하는 건 시간문제일 듯.   
그런데 동일한 카드가 여러 개 있을 때 그 개수를 파악하는 건 아직 어떻게 해야할지 모르겠음.   
   

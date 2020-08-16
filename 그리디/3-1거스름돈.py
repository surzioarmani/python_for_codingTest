/*
2020.08.16
그리디 알고리즘
작성자: 조수아
*/

#예제 3-1 거스름돈 
n = 1260

count = 0;

#큰 단위의 화폐부터 차례대로 확인
list = [500, 100, 50, 10]

for coin in list:
  count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin

print(count)


def solution(amount):
  denominations = [1, 10, 50, 100]
  denominations.sort(reverse=True)  # ❶  화폐 단위를 큰 순서대로 정렬

  change = []  # ❷ 거스름돈을 담을 리스트

  for coin in denominations:
    while amount >= coin:  # ❸ 해당 화폐 단위로 거스름돈을 계속 나눠줌
      change.append(coin)  # ❹ 거스름돈 리스트 업데이트
      amount -= coin  # ❺ 정산이 완료된 거스름돈 뺌
  # ❻ 거스름돈 리스트 반환
  return change

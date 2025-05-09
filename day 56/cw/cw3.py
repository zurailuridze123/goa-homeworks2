def captianjack(gold_coins):
  ships = [150, 200, 250, 300, 350]
  for ship_price in ships:
    if gold_coins >= ship_price:
      print(f"კაპიტანმა ჯეკმა იყიდა გემი {ship_price} ოქროს მონეტით")
      return
  print("ეკიპაჟი აჯანყდა! არ არის საკმარისი ოქროს მონეტებ")


def maxProfit(prices) -> int:

    maxprofit = -1
    days = len(prices)

    while True:
        sellprice = -1
        buyprice_pos = -1
        buyprice = 100000

        for i in range(days):
            if prices[i] < buyprice:
                buyprice = prices[i]
                buyprice_pos = i
        if buyprice_pos == -1:
            break
        for i in range(buyprice_pos + 1,days):
            if prices[i] > buyprice:
                sellprice = prices[i]

        if sellprice == -1:
            continue

        currentprofit = sellprice - buyprice
        if currentprofit > maxprofit:
            maxprofit = currentprofit
        else:
            break

    if maxprofit == -1:
        return 0
    return maxprofit

    """
    Code not working(also don't know why):
    
    total_days = len(prices)
    descending = 1
    for i in range(total_days - 2):
        if prices[i] < prices[i + 1]:
            descending = 0
            break
    if descending == 1:
        print("the price list is descending")
        return 0

    dic_price_to_dates = {}  # key is the price, match price to its date(s), represented by a list
    for i in range(total_days):
        price = prices[i]
        if price not in dic_price_to_dates:
            dic_price_to_dates[price] = []
        dic_price_to_dates[price].append(i)
    sorted_prices = sorted(prices)

    maxprofit = 0
    # 最小的价格，从后往前筛，筛到一个成立的差价即可；再弄第二小的价格，第三小的价格以此类推。
    # 只要成立的差价是这个与最大的价格，并且此差价比之前的差价更大，就返回
    for i in range(total_days):
        cur_min = sorted_prices[i]
        max_index = total_days - 1
        while max_index > i:
            cur_max = sorted_prices[max_index]
            cur_diff = cur_max - cur_min
            if cur_diff <= maxprofit:
                break
            else:  # cur_diff > maxprofit
                date_cur_max = max(dic_price_to_dates[cur_max])
                date_cur_min = min(dic_price_to_dates[cur_min])
                if date_cur_min < date_cur_max:  # 找到成立的差价
                    if cur_max == sorted_prices[total_days - 1]:
                        return cur_diff
                    else:
                        maxprofit = max(maxprofit, cur_diff)
                else:  # 暂时差价不成立
                    max_index -= 1
    return maxprofit
    """


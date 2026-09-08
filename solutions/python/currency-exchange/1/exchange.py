def exchange_money(budget, exchange_rate):
    """Estimate the value of the currency after exchange.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate the amount of money left from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange.
    :return: float - amount left of your starting budget after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of the bills received.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - total value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of whole currency bills received from the amount.

    :param amount: float - the total starting amount.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Calculate the leftover amount that cannot be returned in whole bills.

    :param amount: float - the total starting amount.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of currency after applying exchange rate, fee (spread), and bill denominations.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :param spread: int - percentage taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get in whole bills.
    """
    # 1. حساب سعر الصرف الفعلي بإضافة عمولة المكتب (spread %)
    actual_rate = exchange_rate * (1 + spread / 100)
    
    # 2. حساب الميزانية بعد التحويل
    total_exchanged = budget / actual_rate
    
    # 3. حساب عدد الأوراق النقدية الكاملة التي يمكن الحصول عليها
    number_of_bills = total_exchanged // denomination
    
    # 4. إرجاع القيمة الإجمالية للعملة النقدية كعدد صحيح (int)
    return int(number_of_bills * denomination)
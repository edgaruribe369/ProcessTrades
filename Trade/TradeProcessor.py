
class TradeProcessor:
    '''
     Contains the implementation of Csv based resources which takes in
     a csv file and outputs a processed result to another.
     
    input.csv: <TimeStamp>,<Symbol>,<Quantity>,<Price>
    File.csv: <symbol>,<MaxTimeGap>,<Volume>,<WeightedAveragePrice>,<MaxPrice>

    Attributes:
        trade_provider: A TradeProvider object representing trade data sets.

    :Author: Zach Antonas
    :Contact: zantonas@gmail.com
    '''

    def __init__(self, trade_provider):
        self.trade_provider = trade_provider

    def process_trades(self):
        unsorted_list = self.trade_provider.get_trades()
        sorted_list = self.__sort_list__(unsorted_list)
        grouped_sorted_list = self.__group_sorted_list__(sorted_list)
        return self.__process_grouped_list__(grouped_sorted_list)

    def __sort_list__(self, unsorted_list):
        return sorted(unsorted_list, key=lambda x: (x[0]))

    def __group_sorted_list__(self, sorted_list):
        previous_symbol = sorted_list[0][0]
        grouped_sorted_list = []
        tmp_list = []

        for i in sorted_list:
            if i[0] == previous_symbol:
                tmp_list.append(i)
            else:
                previous_symbol = i[0]
                grouped_sorted_list.append(tmp_list)
                tmp_list = []
                tmp_list.append(i)

        return grouped_sorted_list

    def __max_time_gap__(self, li):
        # List is already sorted, so no need to use the commented code below:
        #tmp_list = []
        #for i in li:
        #    tmp_list.append(i[1])
        #max_time_gap = max(tmp_list) - min(tmp_list)

        time = list(map((lambda x: x[1]), li))
        return max(time) - min(time)

    def __total_shares__(self, li):
        return sum(list(map((lambda x: x[2]), li)))

    def __average_price__(self, li):
        cost_totals = 0
        price_totals = 0

        for i in li:
            cost_totals += i[2] * i[3]
            price_totals += i[3]

        return int(cost_totals / price_totals)

    def __max_price__(self, li):
        return max(list(map((lambda x: x[3]), li)))

    def __process_grouped_list__(self, grouped_sorted_list):
        processed_list = []
        for i in grouped_sorted_list:
            index = i[0][0]
            r = self.__max_time_gap__(i)
            t = self.__total_shares__(i)
            a = self.__average_price__(i)
            m = self.__max_price__(i)
            processed_list.append([index, r, t, a, m])

        return processed_list

    def output(self, processed_list):
        self.trade_provider.save_trades(processed_list)


import Constants as C
from Trade.TradeProvider import TradeProvider


class FileManager(TradeProvider):
    '''
    Responsible for reading and writing csv files.
        
    Attributes:
        input: A string representing the location of the unprocessed csv file.
        ouput: A string representing the output location of the processed csv file.
        
    Author: Zach Antonas
    Contact: zantonas@gmail.com 
    '''

    def __init__(self, f_input=C.F_INPUT, f_output=C.F_OUTPUT):
        self.f_input = f_input
        self.f_output = f_output

    def get_trades(self):
        file_data = []

        with open(self.f_input, 'r') as file:
            for line in file:
                l = (line.split(','))
                timestamp = int(l[0])
                symbol = str(l[1])
                quantity = int(l[2])
                price = int(l[3])
                file_data.append((symbol, timestamp, quantity, price))

        return file_data

    def save_trades(self, processed_list):
        with open(self.f_output, 'w') as file:
            for i in processed_list:
                line = '{symbol},{max_time_gap},{volume},{weighted_average_price},{max_price}\n'.format(
                    symbol=i[0], max_time_gap=i[1], volume=i[2], weighted_average_price=i[3], max_price=i[4])
                file.write(line)

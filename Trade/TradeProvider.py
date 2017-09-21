
from abc import ABCMeta, abstractmethod


class TradeProvider(metaclass=ABCMeta):
    '''
    Abstract class responsible for getting trade information from any trading data resource.
        
    Author: Zach Antonas
    Contact: zantonas@gmail.com 
    '''

    @abstractmethod
    def get_trades(self):
        raise NotImplementedError('users must define get_trades to use this base class')

    @abstractmethod
    def save_trades(self, processed_list):
        raise NotImplementedError('users must define save_trades to use this base class')

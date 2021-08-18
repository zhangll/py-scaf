#!/usr/bin/env python
# coding: utf-8

'''

    utils...
    test

'''

class utils(object):

    def __init__(self):
        pass

    def bulu(self,icon=None,title=None,content=None):
        '''
            pop bubble message with ubuntu notify-send

        '''
        import subprocess
        return subprocess.call([ 'notify-send', '-i', icon, title, content]) 

if __name__ == "__main__":
    utils  =  utils()
    utils.bulu('/tmp/27608.jpg','a','hahhah')



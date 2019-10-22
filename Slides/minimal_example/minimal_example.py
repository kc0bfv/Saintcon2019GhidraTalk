#Documentation here
#@author Author name and email
#@category PCode
#@keybinding 
#@menupath 
#@toolbar 


from __future__ import print_function

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def func_here():
    logger.info("Hello World!")

if __name__ == "__main__":
    func_here()

#! /usr/bin/env python

import os.path
from os.path import expanduser

home = expanduser("~")
SETTINGS = home + "/.asuranzeturix/config.yml"


def main( ):
    print("Yaml irakurtzen")


if __name__ == "__main__":
    if not os.path.isfile(SETTINGS):
        print("Ez da existitzen")
    main()

#!/usr/bin/env python

#    This file is part of 'AS Relationship Handler'
#
#    'IP Topology Map' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    'AS Relationship Handler' is distributed in the hope that it will be
#    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public
#    License along with 'AS Relationship Handler'.  If not, see
#    <http://www.gnu.org/licenses/>.

from bs4 import BeautifulSoup
import urllib2
import re
import bz2
from progressbar import ProgressBar
import os

__author__ = 'secastro'


def get_as_relationship_file(datadir='data'):
    start_url = "http://data.caida.org/datasets/as-relationships/serial-1/"

    response = urllib2.urlopen(start_url)
    html = BeautifulSoup(response.read(), "html.parser")

    link_list = []
    for link in html.findAll('a', text=re.compile('as\-rel\.txt\.bz2$')):
        link_list.append(link['href'])

    selected_link = sorted(link_list, reverse=True)[0]
    # print("AS relationship file: %s" % selected_link)
    output_file = os.path.join(datadir, selected_link.rstrip(".bz2"))

    if not os.path.isfile(output_file):
        block_zs = 1024 * 16
        as_file = urllib2.urlopen(start_url + selected_link)
        file_size = int(as_file.info().getheaders("Content-Length")[0])
        print "Downloading: %s Bytes" % file_size

        pbar = ProgressBar(maxval=file_size).start()
        bz2d = bz2.BZ2Decompressor()
        bytes_read = 0
        with open(output_file, 'wb') as as_out_file:
            while True:
                block = as_file.read(block_zs)
                if not block:
                    break

                bytes_read += len(block)
                pbar.update(bytes_read)
                dblock = bz2d.decompress(block)
                as_out_file.write(dblock)

        pbar.finish()

    return output_file

if __name__ == "__main__":
    print(get_as_relationship_file())
